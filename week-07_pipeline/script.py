# ---- Projet1 Portfolio Ready - Traitement automatique de Leads via Notion ----

#Import
import requests
from datetime import datetime

# =========================
# CONFIG
# =========================
NOTION_TOKEN = "YOUR_NOTION_TOKEN"
DATABASE_ID = "YOUR_DATABASE_ID"
NOTION_VERSION = "2022-06-28"
DRY_RUN = True

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def fetch_leads():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        print("Erreur lors de la lecture de la base Notion :")
        print(response.status_code, response.text)
        raise SystemExit(1)
    
    data = response.json()
    return data["results"]

#==== Pour l'extraction des valeurs ====

def extract_title_value(title_prop):
    title_items = title_prop.get("title", []) if title_prop else []
    return "".join(item.get("plain_text", "") for item in title_items)

def extract_status_value(status_prop):
    status_data = status_prop.get("status") if status_prop else None
    return status_data.get("name", "") if status_data else ""

def extract_number_value(number_prop):
    return number_prop.get("number") if number_prop else None

def extract_date_value(date_prop):
    date_data = date_prop.get("date") if date_prop else None
    return date_data.get("start", "") if date_data else ""

def normalize_status(status):
    return (status or "").strip().lower()


def is_followup_name(name):
    return name.strip().lower().startswith("follow-up :")



def transform_data(results):
    clean_leads = []

    for page in results:
        props = page["properties"]

        lead = {
            "page_id": page["id"],
            "name": extract_title_value(props.get("Name")),
            "status": extract_status_value(props.get("Status")),
            "score": extract_number_value(props.get("Score")),
            "last_contact": extract_date_value(props.get("Last Contact")),
        }

        clean_leads.append(lead)

    return clean_leads

# === Règles métiers === 

def should_relaunch(last_contact_str, status):
    normalized_status = normalize_status(status)

    if normalized_status == "closed":
        return False

    if not last_contact_str:
        return False
    
    # On ne garde que YYYY-MM-DD même si Notion renvoie plus
    last_contact_date = datetime.fromisoformat(last_contact_str[:10]).date()
    today = datetime.today().date()
    delta_days = (today - last_contact_date).days

    return delta_days > 7

def followup_exists(existing_names, lead_name):
    target_name = f"Follow-up : {lead_name}".strip().lower()
    return target_name in existing_names

# ==== Applications des règles ====

def apply_rules(leads):
    status_updates = []
    followups_to_create = []

    existing_names = {lead["name"].strip().lower() for lead in leads if lead["name"]}

    summary = {
        "leads_analyzed": 0,
        "status_updates_count": 0,
        "followups_count": 0,
        "skipped_followups_count": 0,
        "skipped_closed_count": 0,
    }

    for lead in leads:
        score = lead["score"]
        status = (lead["status"] or "").strip()
        last_contact = lead["last_contact"]
        page_id = lead["page_id"]
        name = lead["name"]

        # On ignore les follow-ups déjà créés
        if is_followup_name(name):
            continue

        # Ignore les leads closed
        if normalize_status(status) == "closed":
            summary["skipped_closed_count"] += 1
            if DRY_RUN:
                print(f"[DRY RUN] Ignored closed lead: {name}")
            continue

        new_status = None

        summary["leads_analyzed"] += 1

        # Règle 1 : Hot
        if score is not None and score >= 80:
            new_status = "Hot"
        
        # Règle 2 : Relance prioritaire
        if should_relaunch(last_contact, status):
            new_status = "To relaunch"
        
        # Mise à jour uniquement si changement réel
        if new_status and normalize_status(new_status) != normalize_status(status):
            status_updates.append({
                "page_id": page_id,
                "name": name,
                "old_status": status,
                "new_status": new_status
            })
        
        # Règle 3 : Follow-up si score >= 90
        if score is not None and score >= 90:
            if followup_exists(existing_names, name):
                summary["skipped_followups_count"] += 1
            else:
                followups_to_create.append({"name": name})
                existing_names.add(f"follow-up : {name}".strip().lower())
                summary["followups_count"] += 1

    summary["status_updates_count"] = len(status_updates)

    return status_updates, followups_to_create, summary


# === MAJ du statut ===

def update_status(page_id, lead_name, old_status, new_status):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {
        "properties": {
            "Status": {
                "status": {
                    "name": new_status
                }
            }
        }
    }

    if DRY_RUN:
        print(f"[DRY RUN] Update status: {lead_name} | {old_status} -> {new_status}")
        return
    
    response = requests.patch(url, headers=HEADERS, json=payload, timeout=10)

    if response.status_code != 200:
        print(f"Erreur mise à jour page {page_id}:")
        print(response.status_code, response.text)
    

#=== Recréation du lead à suivre fortement ===
def create_followup(database_id, lead_name):
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": f"Follow-up : {lead_name}"
                        }
                    }
                ]
            },
            "Status": {
                "status": {
                    "name": "New"
                }
            }
        }
    }

    if DRY_RUN:
        print(f"[DRY RUN] Create follow-up: Follow-up : {lead_name}")
        return

    response = requests.post(url, headers=HEADERS, json=payload, timeout=10)

    if response.status_code != 200:
        print(f"Erreur création follow-up pour {lead_name}:")
        print(response.status_code, response.text)



def print_summary(summary):
    print("\n=== RÉSUMÉ ===")
    print(f"Leads analysés : {summary['leads_analyzed']}")
    print(f"Mises à jour de statut : {summary['status_updates_count']}")
    print(f"Follow-ups à créer : {summary['followups_count']}")
    print(f"Follow-ups évités (déjà existants) : {summary['skipped_followups_count']}")
    print(f"Leads ignorés (closed) : {summary['skipped_closed_count']}")


def main():
    results = fetch_leads()
    leads = transform_data(results)

    status_updates, followups_to_create, summary = apply_rules(leads)

    for update in status_updates:
        update_status(
            update["page_id"],
            update["name"],
            update["old_status"],
            update["new_status"]
        )

    for item in followups_to_create:
        create_followup(DATABASE_ID, item["name"])

    print_summary(summary)


if __name__ == "__main__":
    main()
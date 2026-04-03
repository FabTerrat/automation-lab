# -4- Dry-Run, pour ne pas modifier avant d'avoir tester

import requests
import sys

# ⚠️ à remplacer
NOTION_TOKEN = "YOUR_NOTION_TOKEN"
DATABASE_ID = "YOUR_DATABASE_ID"

# -4- Ajout du Dry-Run
DRY_RUN = True


def fetch_data():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers)

    if response.status_code != 200:
        print("Erreur API :", response.status_code)
        print(response.text)
        sys.exit(1)

    return response.json()


# ------------ regle métier ------------------------

def transform_data(data):
    clean_data = []

    for page in data["results"]:
        props = page["properties"]

        # Name (title)
        name = ""
        if props["Name"]["title"]:
            name = props["Name"]["title"][0]["text"]["content"]

        # Status (select)
        status = None
        if props["Status"]["select"]:
            status = props["Status"]["select"]["name"]
        
        # Score (number)
        score = props["Score"]["number"]
        

        clean_data.append({
            "page_id": page["id"],
            "name": name,
            "status": status,
            "score": score
        })

    return clean_data


def update_status(page_id, new_status):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    payload = {
        "properties" : {
            "Status" : {
                "select": {
                    "name": new_status
                }
            }
        }
    }

    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code != 200:
        print (f"Erreur update de page {page_id}: {response.status_code}")
        print (response.text)
        return False
    
    return True


# application des règles métiers à la base existante

def apply_rules_and_update(clean_data):
    for item in clean_data : 
        score = item["score"]
        current_status = item["status"]

        if score is None:
            continue

        if score is not None and score >= 80 and current_status != "Hot":
            print (f"Update: {item['name']} | score={score} | {current_status} -> Hot ")

            if DRY_RUN:
                print("DRY RUN → aucune modification envoyée\n")
            else :
                success = update_status(item["page_id"], "Hot")

                if success:
                    print ("Mise à jour OK\n")
                else:
                    print ("Echec de la mise à jour\n")


# ------------ Main ------------------------

def main():
    data = fetch_data()
    clean = transform_data(data)

    print("\nDonnées propres : \n")
    for item in clean :
        print(item)
    
    print("\nApplication des règles...\n")
    apply_rules_and_update(clean)

if __name__ == "__main__":
    main()
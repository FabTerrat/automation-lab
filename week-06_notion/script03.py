# -3- Mettre à jour Notion automatiquement

import requests
import sys

# ⚠️ à remplacer
NOTION_TOKEN = "YOUR_NOTION_TOKEN"
DATABASE_ID = "YOUR_DATABASE_ID"

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
            # -3- Ici on va rajouter l'ID de la page
            "page_id": page["id"],
            "name": name,
            "status": status,
            "score": score
        })

    return clean_data

# ----  Créer la fonction d’update

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


# Ajout d'une regle métier simple 

def apply_rules_and_update(clean_data):
    for item in clean_data : 
        score = item["score"]
        current_status = item["status"]

        if score is not None and score >= 80 and current_status != "Hot":
            print (f"Update: {item['name']} | score={score} | {current_status} -> Hot ")
            success = update_status(item["page_id"], "Hot")

            if score is None:
                continue

            if success:
                print ("Mise à jour OK")
            else:
                print ("Echec de la mise à jour")


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
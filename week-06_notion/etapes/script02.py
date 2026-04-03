# -2- Appliquer la première regle métier pour extraire et lire les données PROPREMENT

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
            "name":name,
            "status":status,
            "score":score
        })

    return clean_data


# ------------ Main ------------------------

def main():
    data = fetch_data()

    clean = transform_data(data)

    print("\nDonnées propres : \n")
    for item in clean :
        print(item)

if __name__ == "__main__":
    main()
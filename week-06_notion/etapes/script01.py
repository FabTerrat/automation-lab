# 1-- Pour bien extraire le json de l'API Notion

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



# ------------ Main ------------------------

def main():
    data = fetch_data()

    # inspection (très important)
    print("Nombre d'items :", len(data["results"]))
    print("\nExemple brut :\n")
    print(data["results"][0])

if __name__ == "__main__":
    main()
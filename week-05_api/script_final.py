import requests
import csv 
import argparse

# URL = "https://jsonplaceholder.typicode.com/users"   --> Ne prenait ici que les users (mis ensuite dans main pour choisir quoi pendre grâce à argparse)


def fetch_data(url):
    #response = requests.get(URL)
    #Ajout d'un temps de 10sec max pour appeler l'API (erreur sinon)
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("Erreur API :", response.status_code)
        exit()

    return response.json()


def transform_data(data):

    clean_users = []

    for user in data:
        clean_user = {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "company": user["company"]["name"],
            "city": user["address"]["city"]
        }
        
        clean_users.append(clean_user)

    return clean_users

def export_csv(clean_users):
    
    output_file = "users_export.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=clean_users[0].keys())

        writer.writeheader()
        writer.writerows(clean_users)

    print("Export terminé : ", output_file)


# --- fonction principale ---

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--endpoint",
        default="users",
        help="API endpoint to fetch (users, posts, comments)"
    )

    args = parser.parse_args()

    url = f"https://jsonplaceholder.typicode.com/{args.endpoint}"

    data = fetch_data(url)

    clean_users = transform_data(data)

    export_csv(clean_users)

if __name__ == "__main__":
    main()
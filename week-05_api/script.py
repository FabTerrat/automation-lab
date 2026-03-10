import requests
import csv 

URL = "https://jsonplaceholder.typicode.com/users"


def fetch_data():
    response = requests.get(URL)

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
    data = fetch_data()

    clean_users = transform_data(data)

    export_csv(clean_users)

if __name__ == "__main__":
    main()
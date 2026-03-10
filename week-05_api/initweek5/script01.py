import csv

# --- Importation et première lecture des données provenant de l'API ---
import requests

URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(URL)

# -- anticipation d'erreur --
if response.status_code != 200:
    print("Erreur API :", response.status_code)
    exit()

print(response.status_code)

data = response.json()

# print(data)
#print(len(data))
#print(data[0])

# --- Transformation des données, création d'une liste propre de dictionnaire ---

clean_users = []

for user in data : 

    clean_user = {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "company": user["company"]["name"],
        "city": user["address"]["city"]
    }

    clean_users.append(clean_user)

print(clean_users)


# --- Ajout de la fonction d'export ---

output_file = "users_export.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file :
    writer = csv.DictWriter(file, fieldnames=clean_users[0].keys())

    writer.writeheader()
    writer.writerows(clean_users)

print("Export CSV terminé :", output_file)

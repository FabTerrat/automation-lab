#------------------Ouverture et lecture du fichier CS--------------------------

import csv

INPUT_FILE = "input.csv"

with open (INPUT_FILE, mode="r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("Nombre de lignes lues :", len(rows))
print("Première ligne:", rows[0])


#------------------filtrage des scores-------+Réécriture du mail en minuscule-------------------
filtered_rows = []

for row in rows:
    score = int(row["score"])

    if score >= 80 :
        row["email"] = row["email"].lower()
        filtered_rows.append(row)

print("Lignes après filtrage :", len(filtered_rows))
print("Exemple ligne filtrée", filtered_rows[0])

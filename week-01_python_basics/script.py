#optionnel -- ajout du système d'erreur try
import sys

#------------------Ouverture et lecture du fichier CS--------------------------
import csv
INPUT_FILE = "input.csv"

#Ajout de l'erreur possible 
try :

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

    #------------------Création nouveau CSV propre-----------------------

    OUTPUT_FILE = "output_clean.csv"

    with open(OUTPUT_FILE, mode="w", encoding="utf-8", newline="") as f:
        fieldnames = ["nom", "email", "score"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(filtered_rows)

    print("Fichier output_clean.csv généré")

#Formalisation de l'erreur si existante
except Exception as e:
    print ("❌ Erreur lors de l’exécution du script")
    print ("detail :", e)
    sys.exit(1)
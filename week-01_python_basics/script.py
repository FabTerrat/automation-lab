import csv

INPUT_FILE = "input.csv"

with open (INPUT_FILE, mode="r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("Nombre de lignes lues :", len(rows))
print("Première ligne:", rows[0])

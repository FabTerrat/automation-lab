from pathlib import Path
from collections import Counter

INPUT_DIR = Path("input_raw")
OUTPUT_DIR = Path ("output_clean")

#Table de routage : extension -> sous-dossier cible
ROUTES = {
    ".pdf": "pdf",
    ".csv": "data",
    ".xlxs": "data",
    ".png": "images",
    ".jpeg": "images",
    ".jpg": "images",
    ".txt": "other",
}

def classify(ext: str) -> str:
    """Retourne le sous-dossier cible selon l'extension"""
    return ROUTES.get(ext, "other")

if not INPUT_DIR.exists():
    print("❌ Le dossier input_raw n'existe pas")
    raise SystemExit(1)

#Crée le dossier de sortie si besoin (sans erreur s'il existe)
OUTPUT_DIR.mkdir(exist_ok=True)

files = [p for p in INPUT_DIR.iterdir() if p.is_file()]

print ("📂 Plan de tri (aucun déplacement pour l’instant) :")
targets=[]

for p in files:
    ext = p.suffix.lower() if p.suffix else ""
    bucket = classify(ext)
    target_dir = OUTPUT_DIR / bucket
    targets.append(bucket)

    print(f"- {p.name} -> {bucket}/")

#Stats sur les destinations 
counts = Counter(targets)

print("\n📊 Répartition prévue :")
for bucket, count in counts.most_common():
    print(f"- {bucket}/: {count}")

print("\n✅ OK — étape 3 : règles de tri prêtes.")


from pathlib  import Path
from collections import Counter

# INPUT_DIR = Path("input_raw")
# OUTPUT_DIR = Path("output_clean")
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input_raw"
OUTPUT_DIR = BASE_DIR / "output_clean"

DRY_RUN = False #✅ True = simulation, False = exécution réelle

#Test 
print("DEBUG: script lancé depuis :", Path.cwd())
print("DEBUG: INPUT_DIR absolu :", INPUT_DIR.resolve())

ROUTES = {
    ".pdf": "pdf",
    ".csv": "data",
    ".xlxs": "data",
    ".png": "images",
    ".jpeg": "images",
    ".jpg": "images",
    ".txt": "other",
}

def classify(ext : str) -> str :
    return ROUTES.get(ext,"other")

def ensure_dir(path : Path) -> None :
    """Crée un dossier s'il n'existe pas."""
    path.mkdir(parents=True, exist_ok=True)

if not INPUT_DIR.exists() :
    print("❌ Le dossier input_raw n'existe pas")
    raise SystemExit(1)

ensure_dir(OUTPUT_DIR) #Crée le fichier "output_clean" s'il n'existe pas

files= [p for p in INPUT_DIR.iterdir() if p.is_file()]
if not files:
    print("ℹ️ Aucun fichier à traiter. Dossier déjà propre.")
    raise SystemExit(0)

print ("📦 Tri des fichiers :")
moved_targets = []

for src in files:
    # ext = src.suffix.lower if src.suffix else ""
    print(f"\nDEBUG src.name = {src.name}")
    print(f"DEBUG src.suffix = {src.suffix!r}")
    print(f"DEBUG src.stem = {src.stem!r}")

    ext = src.suffix.lower() if src.suffix else ""
    print(f"DEBUG ext calculée = {ext!r}")
    bucket = classify(ext)

    dest_dir = OUTPUT_DIR / bucket
    ensure_dir(dest_dir) # Crée le/les dossiers fils s'ils n'existent pas 

    dest = dest_dir / src.name

    #Sécurité anti-écrasement : si le fichier existe déjà, on le renomme
    if dest.exists():
        dest = dest_dir / f"{src.stem}_DUP{src.suffix}"

    moved_targets.append(bucket)

    if DRY_RUN : 
        print(f"🟡 [DRY RUN] {src.name}  →  {bucket}/")
    else:
        src.rename(dest) # déplace (dans le même disque) et renomme si besoin
        print(f"🟢 Déplacé : {src.name}  →  {bucket}/")

counts = Counter(moved_targets)

print("\n📊 Répartition :")
for bucket, count in counts.most_common():
    print(f"- {bucket}/:{count}")

if DRY_RUN:
    print("\n✅ Simulation terminée. Mets DRY_RUN = False pour exécuter.")
else:
    print("\n✅ Tri terminé.")

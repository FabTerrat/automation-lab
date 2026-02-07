from pathlib import Path
from collections import Counter

# 1. Chemin vers le dossier à analyser
INPUT_DIR = Path("input_raw")

# 2. Vérification que le dossier existe
if not INPUT_DIR.exists():
    print("❌ Le dossier input_raw n'existe pas")
    ## exit(1)
    raise SystemExit(1)

# # 3. Lister les fichiers
# print("📂 Fichiers trouvés :")

# for file in INPUT_DIR.iterdir():
#     if file.is_file():
#         print("-", file.name)

#-----------------------Phase 2-----------------Classer “sur le papier” : extensions + inventaire -----

files = [p for p in INPUT_DIR.iterdir() if p.is_file()]

print("📂 Fichiers trouvés :")
for p in files:
    ext = p.suffix.lower() if p.suffix else "(sans extension)"
    print(f"- {p.name}  →  {ext}")

# Compter les extensions        (Counter produit un dictionnaire qui compte chaque terme)
ext_counts = Counter(
    (p.suffix.lower() if p.suffix else "(sans extension)")
    for p in files
)

print("\n📊 Résumé par type :")
for ext, count in ext_counts.most_common():
    print(f"- {ext}: {count}")


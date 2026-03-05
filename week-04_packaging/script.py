import argparse
import sys
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "../data/input_leads.csv"
DEFAULT_OUTPUT = BASE_DIR / "output_report.xlsx"

# ---- ajout d'arguments - fonction pour appeler n'importe quel fichier en entrée, et/ou en sortie ----
def parse_args():
    parser = argparse.ArgumentParser(
        description="Génère un rapport Excel multi-feuilles à partir d'un CSV de leads."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default=str(DEFAULT_INPUT),
        help="Chemin du fichier CVS d'entrée (défaut: input_leads.csv dans le dossier data en amont).",
    )
    parser.add_argument(
        "output",
        nargs="?",
        default=str(DEFAULT_OUTPUT),
        help="Chemin du fichier Excel de sortie (défaut: output_report.xlsx dans le dossier du script).",
    )

    # --- AJout des éléments de cadrage
    #option --delimiter (utile si un client a des CSV en ;)
    parser.add_argument(
        "--delimiter",
        default=",",
        help="Délimiteur CSV (défaut: ','). Exemple courant en FR: ';'.",
    )

    #option --dry-run (comme semaine 2 : très pro)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simule l'exécution : valide l'entrée et calcule les tables sans écrire dans l'Excel.",
    )

    return parser.parse_args()


# ---- Règles métier ----
def compute_metrics(df):
    # --- Filtre métier ---
    qualified_leads = df[df["status"] == "Qualified"]

    # --- KPIs ---
    total_leads = len(df)
    average_score = df["score"].mean()

    kpis = pd.DataFrame([
        {"metric": "total_leads", "value": total_leads},
        {"metric": "average_score", "value": round(average_score, 2)}
    ])

    # --- Aggregation --- 
    by_status = (
        df["status"]
        .value_counts()
        .rename_axis("status")
        .reset_index(name="count")
    )

    by_source = (
        df["source"]
        .value_counts()
        .rename_axis("source")
        .reset_index(name="count")
    )

    return kpis, by_status, by_source, qualified_leads

# ---- export/report function ----
def export_report(output_file, kpis, by_status, by_source, qualified_leads):

    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer :
        kpis.to_excel(writer, sheet_name="KPIs", index=False)
        by_status.to_excel(writer, sheet_name="By Status", index=False)
        by_source.to_excel(writer, sheet_name="By Source", index=False)
        qualified_leads.to_excel(writer, sheet_name="Qualified", index=False)


# ---- MAIN function ----------------------------------------------------------
def main():

    args = parse_args()

    input_file = Path(args.input)
    output_file = Path(args.output)

    # UX: on montre toujours ce qui va être utilisé
    print(f"📥 Input : {input_file}")
    print(f"📤 Output: {output_file}")

    # 1) Validation entrée
    if not input_file.exists():
        print(f"❌ Fichier d'entrée introuvable : {input_file}")
        sys.exit(2)
    if not input_file.is_file():
        print(f"❌ L'entrée n'est pas un fichier : {input_file}")
        sys.exit(2)


    # 2) Lecture CSV (robuste)
    try:
        df = pd.read_csv(input_file, sep=args.delimiter, encoding="utf-8")
    except Exception as e:
        print(f"❌ Impossible de lire le CSV ({input_file.name}) : {e}")
        sys.exit(1)


    # 3) Calculs métier
    try: 
        kpis, by_status, by_source, qualified_leads = compute_metrics(df)
    except KeyError as e:
        print(f"❌ Colonne manquante dans le CSV : {e}")
        print("➡️ Colonnes attendues : status, source, score")
        sys.exit(2)
    except Exception as e:
        print(f"❌ Erreur lors des calculs : {e}")
        sys.exit(1)

    if args.dry_run:
        print("🟡 DRY RUN: aucun fichier Excel n'a été généré.")
        print(f"✅ Lignes totales : {len(df)} | Leads qualifiés : {len(qualified_leads)}")
        sys.exit(0)

    # 4) Prépare la sortie (crée le dossier si nécessaire)
    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"❌ Impossible de créer le dossier de sortie : {e}")
        sys.exit(1)

    # 5) Export
    try:
        export_report(output_file, kpis, by_status, by_source, qualified_leads)
        print(f"✅ Rapport Excel généré : {output_file.name}")
    except Exception as e:
        print(f"❌ Erreur lors de l'export Excel : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

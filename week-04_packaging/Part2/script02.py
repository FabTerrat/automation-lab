import pandas as pd
import sys
from pathlib import Path
# ajout
import argparse

# ----les constantes ----
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input_leads.csv"

# ---- ajout d'arguments - fonction pour appeler n'importe quel fichier en entrée, et/ou en sortie ----
def parse_args():
    parser = argparse.ArgumentParser(
        description="Génère un rapport Excel multi-feuilles à partir d'un CSV de leads."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default=str(INPUT_FILE),
        help="Chemin du fichier CVS d'entrée (défaut: input_leads.csv dans le dossier de script).",
    )
    parser.add_argument(
        "output",
        nargs="?",
        default=str(BASE_DIR / "output_report.xlsx"),
        help="Chemin du fichier Excel de sortie (défaut: output_report.xlsx dans le dossier du script).",
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
    
    print(f"✅ Rapport Excel généré : {output_file.name}")


# ---- MAIN function ----------------------------------------------------------
def main():
    try:
        args = parse_args()

        input_file = Path(args.input)
        output_file = Path(args.output)

        # option pro - check d'existence
        if not input_file.exists():
            print(f"❌ Fichier d'entrée introuvable : {input_file}")
            sys.exit(1)

        df = pd.read_csv(input_file)

        kpis, by_status, by_source, qualified_leads = compute_metrics(df)

        export_report(
            output_file,
            kpis,
            by_status,
            by_source,
            qualified_leads
        )        

        # Optionnel : pour bien voir les entrées et sorties définies
        print(f"📥 Input: {input_file}")
        print(f"📤 Output: {output_file}")

    except Exception as e: 
        print(f"Erreur lors du traitement : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

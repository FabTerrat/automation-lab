import pandas as pd
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input_leads.csv"
OUTPUT_FILE = BASE_DIR / "output_report.csv"

def main():
    try:
        df = pd.read_csv(INPUT_FILE)

        print("Fichier chargé")

        # --- KPIs ---
        total_leads = len(df)
        average_score=df["score"].mean()

        # --- Agrégations ---
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

        # --- Construction du rapport (format "long") --- 
        kpi_block = pd.DataFrame([
            {"metric": "total_leads", "value": total_leads},
            {"metric": "average_score", "value": round(average_score, 2)}
        ])

        # On ajoute une colonne "section" pour que le CSV soit lisible 
        kpi_block.insert(0, "section", "kpis")
        by_status.insert(0, "section", "by_status")
        by_source.insert(0, "section", "by_source")

        report = pd.concat([kpi_block, by_status, by_source], ignore_index=True)

        report.to_csv(OUTPUT_FILE, index=False)

        print(f"✅ Rapport généré : {OUTPUT_FILE.name}")

    except Exception as e: 
        print(f"Erreur lors du traitement : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

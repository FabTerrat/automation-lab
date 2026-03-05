import pandas as pd
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input_leads.csv"
# OUTPUT_FILE = BASE_DIR / "output_report.csv"

def main():
    try:
        df = pd.read_csv(INPUT_FILE)

        # --- Filtre métier ---
        qualified_leads = df[df["status"] == "Qualified"]

        # --- KPIs ---
        total_leads = len(df)
        average_score = df["score"].mean()

        kpis = pd.DataFrame([
            {"metric": "total_leads", "value": total_leads},
            {"metric": "average_score", "value": round(average_score, 2)}
        ])

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

        # --- Export Excel multi-feuilles --- 
        output_file = BASE_DIR / "output_report.xlsx"

        with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
            kpis.to_excel(writer, sheet_name="KPIs", index=False)
            by_status.to_excel(writer, sheet_name="By Status", index=False)
            by_source.to_excel(writer, sheet_name="By Source", index=False)
            qualified_leads.to_excel(writer, sheet_name="Qualified", index=False)

        print(f"✅ Rapport Excel généré : {output_file.name}")
        

    except Exception as e: 
        print(f"Erreur lors du traitement : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

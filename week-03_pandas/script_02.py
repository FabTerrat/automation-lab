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
        
        # 1. Nombre total de leads
        total_leads = len(df)
        
        # 2. Répartition par statut
        leads__by_status = df ["status"].value_counts()

        # 3. Score moyen
        average_score = df["score"].mean()

        # 4. Top sources
        leads_by_source = df["source"].value_counts()

        print("\n📊 Indicateurs clés")
        print(f"Nombre total de leads : {total_leads}\n")

        print("répartition par statut : ")
        print(leads__by_status, "\n")

        print(f"Score moyen des leads : {average_score:.1f}\n")

        print("Répartition par source : ")
        print(leads_by_source)


    except Exception as e: 
        print(f"Erreur lors du traitement : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

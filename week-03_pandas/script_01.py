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
        print(df.head())

    except Exception as e: 
        print(f"Erreur lors du traitement : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

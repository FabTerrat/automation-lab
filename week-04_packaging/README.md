# Week 04 — Packaging : rapport Excel automatisé (outil réutilisable)

## Problème
Produire un reporting (KPIs + répartitions + liste des leads qualifiés) à partir d’un CSV prend du temps, génère des erreurs et n’est pas reproductible.

## Solution
Un script Python réutilisable qui :
- lit un fichier CSV de leads
- calcule des KPIs et agrégations
- génère un Excel multi-feuilles prêt à être partagé

## Entrée attendue (CSV)
Colonnes attendues :
- `status`
- `source`
- `score`

## Sortie (Excel)
Le fichier Excel contient 4 onglets :
- `KPIs`
- `By Status`
- `By Source`
- `Qualified`

## Utilisation

### Exécution simple (valeurs par défaut)
```bash
python script.py

---

### Spécifier un fichier d’entrée
```bash
python script.py "../data/mes_leads.csv"

### Spécifier entrée + sortie
```bash
python script.py ../data/mes_leads.csv rapport.xlsx

### CSV avec séparateur ; (fréquent en France)
```bash
python script.py ../data/mes_leads.csv rapport.xlsx --delimiter ";"

### Mode simulation (ne génère pas l’Excel)
```bash
python script.py mes_leads.csv rapport.xlsx --dry-run


---

pip install -r requirements.txt
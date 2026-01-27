# Semaine 1 — Nettoyage et structuration de données CSV

## Description
Ce script Python permet de nettoyer et structurer automatiquement des données issues d’un fichier CSV.

Il :
- lit un fichier CSV brut
- filtre les lignes selon une règle métier (score ≥ 80)
- normalise les adresses email (minuscules)
- génère un nouveau fichier CSV propre en sortie

---

## Fonctionnement
1. Lecture d’un fichier CSV d’entrée
2. Filtrage des données selon un seuil de score
3. Normalisation des emails
4. Génération d’un fichier CSV de sortie contenant uniquement les données pertinentes

---

## Lancement du script
1. Se placer dans le dossier `week-01_python_basics`
2. Vérifier que `script.py` et `input.csv` sont dans le même dossier
3. Lancer la commande :

```bash
python script.py
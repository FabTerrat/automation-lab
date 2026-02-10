# Automatisation de reporting de leads commerciaux

## 🎯 Problème métier

Chaque semaine, l’équipe commerciale exporte un fichier de leads (CSV) depuis un CRM ou un outil marketing.
Le reporting est ensuite fait manuellement dans Excel :
- tris et filtres à la main
- calculs répétés
- risque d’erreur
- perte de temps
- résultats peu reproductibles

## 💡 Solution

Ce script automatise entièrement le reporting à partir d’un simple fichier CSV :
- calcul des indicateurs clés
- agrégations par statut et par source
- génération d’un fichier Excel multi-feuilles, prêt à être utilisé ou envoyé

Aucune manipulation manuelle dans Excel n’est nécessaire.

## 📥 Entrée

Un fichier CSV de leads contenant au minimum les colonnes suivantes :
- `date` : date de création du lead
- `source` : origine du lead (Website, LinkedIn, etc.)
- `status` : statut commercial (New, Qualified, Won, Lost)
- `score` : score de qualification
- `owner` : commercial en charge

Exemple : `input_leads.csv`

## ⚙️ Traitement automatisé

Le script effectue les actions suivantes :
1. Lecture du fichier CSV
2. Calcul des KPIs globaux :
   - nombre total de leads
   - score moyen
3. Agrégation des leads :
   - par statut
   - par source
4. Filtrage métier :
   - extraction des leads avec le statut **Qualified**
5. Génération d’un fichier Excel structuré

## 📤 Sortie

Un fichier Excel `output_report.xlsx` contenant 4 onglets :

- **KPIs**
  - Vue synthétique pour le management
- **By Status**
  - Répartition des leads par statut
- **By Source**
  - Répartition des leads par source
- **Qualified**
  - Liste complète des leads qualifiés, prête pour l’action commerciale

## 🚀 Exécution

Depuis le dossier `week-03_pandas/` :

```bash
python script.py

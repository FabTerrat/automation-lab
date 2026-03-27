Automatisation de pipeline de leads (Notion)
🎯 Problème

Dans de nombreux contextes freelance ou startup, les leads sont stockés dans un outil comme Notion, mais :

aucun système de priorisation clair
relances oubliées
pipeline peu fiable
temps perdu à décider quoi faire

👉 Résultat : des opportunités manquées et un suivi inefficace.

💡 Solution

Ce script automatise la gestion d’un pipeline de leads directement dans Notion.

Il permet de :

prioriser automatiquement les leads
identifier les relances nécessaires
générer des actions de suivi
maintenir un pipeline à jour sans intervention manuelle
⚙️ Fonctionnement

Pipeline complet :

Notion → extraction des données → règles métier → actions → résumé
Entrée

Base Notion avec les propriétés :

Name (title)
Status (status)
Score (number)
Last Contact (date)
Règles métier
1. Qualification automatique
Si Score ≥ 80 → Status = "Hot"
2. Relance automatique
Si dernier contact > 7 jours ET Status ≠ Closed
→ Status = "To relaunch"
3. Création de follow-up
Si Score ≥ 90 → création d’une tâche :
"Follow-up : {Name}"
4. Exclusion des leads fermés
Si Status = Closed → aucune action
Sortie
mise à jour des statuts dans Notion
création de nouvelles tâches de suivi
résumé des actions effectuées
🔒 Sécurité
Mode DRY_RUN pour tester sans modifier les données
évite les doublons de follow-ups
ignore les leads déjà traités ou fermés
📊 Exemple de sortie
=== RÉSUMÉ ===
Leads analysés : 8
Mises à jour de statut : 5
Follow-ups à créer : 2
Follow-ups évités (déjà existants) : 3
Leads ignorés (closed) : 1
💼 Cas d’usage
Freelance : gestion de prospects
Sales : priorisation du pipeline
Startup : automatisation CRM léger
Ops : suivi d’opportunités
🚀 Valeur apportée
gain de temps (moins de traitement manuel)
réduction des erreurs humaines
priorisation claire et automatique
meilleure conversion des leads
🧱 Stack technique
Python
API Notion
requests
🔧 Lancer le script
Configurer :
NOTION_TOKEN = "..."
DATABASE_ID = "..."
Lancer :
python script.py
⚠️ Limites actuelles
follow-ups créés dans la même base (architecture simple)
anti-doublon basé sur le nom
pas de pagination Notion

👉 Ces points peuvent être améliorés selon le contexte client.

🧠 Auteur

Projet réalisé dans une démarche d’automatisation métier orientée freelance :

simplicité
maintenabilité
valeur business
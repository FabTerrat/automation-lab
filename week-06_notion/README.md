# Automatisation Notion — Qualification et suivi de leads

## 🎯 Objectif

Automatiser la gestion d’une base de leads dans Notion :

- qualification automatique des leads selon leur score
- mise à jour du statut
- création de follow-ups pour les leads prioritaires

---

## ⚙️ Fonctionnement

Le script :

1. Récupère les données depuis une base Notion
2. Transforme le JSON en structure exploitable
3. Applique des règles métier :
   - score ≥ 80 → statut = "Hot"
   - score ≥ 90 → création d’un follow-up
4. Met à jour ou crée les éléments dans Notion

---

## 🧠 Règles métier

- Leads chauds → priorisation automatique
- Leads très chauds → création d’une action de suivi

---

## 🛠️ Stack

- Python
- Notion API
- requests

---

## ▶️ Installation

```bash
pip install -r requirements.txt


## ▶️ Configuration
Modifier dans le script :
NOTION_TOKEN = "YOUR_NOTION_TOKEN"
DATABASE_ID = "YOUR_DATABASE_ID"

## ▶️ Exécution
python script.py


## 🔒 Sécurité
Le script inclut un mode :
DRY_RUN = True

Permet de :
tester les règles métier
éviter toute modification réelle


## 💼 Cas d’usage
CRM simple (Notion)
qualification de leads
gestion de pipeline
automatisation de suivi commercial

##⚠️ Limites
pas de gestion des doublons à la création
dépend des noms exacts des propriétés Notion
pas de gestion multi-bases

##🚀 Améliorations possibles
ajout d’un mode CLI (--dry-run)
gestion des doublons
séparation en plusieurs bases (Leads / Follow-ups)
sécurisation via variables d’environnement

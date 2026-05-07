# Lead Qualification Automation — Make + Python

Automatisation hybride permettant de qualifier et prioriser automatiquement des leads entrants via une logique métier Python intégrée à Make, avec restitution dans Notion.

---

## 🎯 Objectif

Réduire le temps passé à trier manuellement les leads entrants et identifier rapidement les opportunités à forte valeur.

---

## ⚙️ Stack

- Google Forms / Google Sheets
- Make
- Python + Flask
- ngrok
- Notion

---

## 🧱 Workflow

```text
Google Form
→ Google Sheets
→ Make
→ API Python Flask
→ Notion

## 🧠 Fonctionnement

Chaque lead est analysé selon plusieurs critères :

budget
urgence
type de besoin
qualité du message
email professionnel ou personnel

L’API retourne :

un score
un niveau de priorité
un segment
une explication du scoring

## ✅ Fonctionnalités
qualification automatique des leads
scoring métier personnalisé
gestion multi-catégories
anti-doublons via email
logs simples
gestion d’erreurs API

## 📊 Exemple de résultat
{
  "success": true,
  "score": 100,
  "priority": "High",
  "segment": "Qualified Lead",
  "reason": "Budget élevé, urgence forte, besoin orienté automatisation."
}

##  🚀 Lancer le projet
Installer les dépendances: pip install -r requirements.txt
Lancer Flask: python app.py
Exposer avec ngrok: ngrok http 5000

## 💼 Valeur apportée
réduction du tri manuel
meilleure priorisation commerciale
centralisation des leads enrichis
gain de temps opérationnel

## 🔜 Améliorations possibles
hébergement cloud
notifications Slack
scoring dynamique
dashboard
monitoring
```

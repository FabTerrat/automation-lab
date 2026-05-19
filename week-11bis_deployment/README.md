# Lead Qualification API — Deployment Version

Automatisation hybride permettant de qualifier et prioriser automatiquement des leads entrants via une API Python déployée dans le cloud.

---

## 🎯 Objectif

Réduire le temps de tri manuel des leads et améliorer la priorisation commerciale grâce à un scoring automatisé.

---

## ⚙️ Stack

- Google Forms / Google Sheets
- Make
- Python + Flask
- Render
- Notion

---

## 🧱 Architecture

```text
Google Form
→ Google Sheets
→ Make
→ API Flask déployée sur Render
→ Notion


## 🧠 Fonctionnalités
qualification automatique des leads
scoring métier personnalisé
gestion multi-catégories
anti-doublons via email
logs simples
gestion d’erreurs API
endpoint sécurisé par token
API déployée dans le cloud


## 🔐 Sécurité

L’API est protégée via un token transmis dans les headers HTTP :

Authorization: Bearer <API_TOKEN>

Les secrets sont stockés via variables d’environnement.


## 🚀 Déploiement

API Flask déployée sur Render avec :

gunicorn
port dynamique
variables d’environnement
URL publique stable

Exemple d’endpoint :

https://lead-qualification-api.onrender.com/score


## 📊 Exemple de réponse
{
  "success": true,
  "score": 100,
  "priority": "High",
  "segment": "Qualified Lead",
  "reason": "Budget élevé, urgence forte, besoin orienté automatisation."
}


## 💼 Valeur apportée
réduction du tri manuel
meilleure priorisation des opportunités
centralisation des leads enrichis
workflow autonome et déployé
automatisation plus crédible en contexte client


## 🔜 Améliorations possibles
notifications Slack / email
scoring IA
dashboard de suivi
monitoring
gestion avancée des erreurs
hébergement base de données
```

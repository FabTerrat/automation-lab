Qualification automatique de leads

🎯 Problème

Lorsque des leads arrivent en continu (formulaire, contact, inbound), il devient difficile de :

savoir lesquels traiter en priorité
identifier les opportunités à forte valeur
éviter de perdre du temps sur des leads peu qualifiés

👉 Résultat : perte de temps + opportunités manquées

💡 Solution

Mise en place d’un système d’automatisation qui :

analyse automatiquement chaque lead entrant
attribue un score basé sur des critères métier
classe les leads selon leur priorité
centralise les résultats dans Notion

👉 Le tri et la priorisation sont faits automatiquement, sans intervention manuelle

⚙️ Fonctionnement
Formulaire → Google Sheets → Make → API Python → Notion

Détail :

Un lead est soumis via un formulaire
Il est stocké dans Google Sheets
Make détecte une nouvelle entrée
Make envoie les données à une API Python
Python analyse le lead (scoring)
Le résultat est renvoyé à Make
Le lead enrichi est enregistré dans Notion
🧠 Logique métier

Chaque lead est évalué selon plusieurs critères :

budget
niveau d’urgence
type de besoin
qualité du message
email professionnel ou non

Le système retourne :

un score (0 à 100)
un niveau de priorité (Low / Medium / High)
un segment (Unqualified / Potential / Qualified)
une explication du score

📊 Résultat
priorisation automatique des leads
gain de temps sur le tri manuel
meilleure prise de décision
focus sur les leads à forte valeur


🛠️ Stack technique
Google Forms / Sheets (entrée de données)
Make (orchestration)
Python + Flask (logique métier)
ngrok (exposition API locale)
Notion (visualisation des résultats)


🚀 Lancer le projet (local)
1. Installer les dépendances
pip install -r requirements.txt
2. Lancer l’API Python
python app.py
3. Exposer avec ngrok
ngrok http 5000
4. Configurer Make

Trigger : Google Sheets (new row)
Action : HTTP request vers /score
Action : création dans Notion

⚠️ Limites actuelles
pas de gestion d’erreurs avancée
pas de fallback si l’API est indisponible
gestion des multi-valeurs simplifiée
pas d’anti-doublons

👉 améliorations prévues pour la semaine suivante

💼 Cas d’usage
freelances recevant des demandes clients
équipes commerciales
agences
recruteurs
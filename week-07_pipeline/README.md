Automatisation de pipeline de leads (Notion)
🔴 Problème

Le client gère un volume croissant de leads dans sa base de données, qu’il doit traiter manuellement.
Il doit décider lui-même quels leads sont prioritaires, quand les relancer et comment les suivre.

Résultat :

perte de temps
charge mentale élevée
risques d’oublis ou de mauvaise priorisation


🟢 Solution

Mise en place d’une automatisation qui analyse les leads en continu et applique des règles métier pour les qualifier et déclencher des actions.

Le système :

classe automatiquement les leads selon leur score
déclenche des relances en cas d’inactivité
crée des suivis pour les leads prioritaires
évite les doublons et les erreurs


⚙️ Règles métier

Si le score ≥ 80 → le lead est automatiquement marqué comme “Hot”
Si aucune interaction depuis plus de 7 jours → une relance est déclenchée
Si le score ≥ 90 → un follow-up dédié est créé
Si le lead existe déjà → aucun doublon n’est créé
Si le statut est “Closed” → le lead est exclu du traitement


🎯 Résultat

réduction significative du temps de traitement des leads
suppression de la charge mentale liée au suivi manuel
priorisation automatique des leads à fort potentiel
plus aucun lead oublié ou non relancé
base de données toujours propre et exploitable
diminution des erreurs humaines dans le suivi


🛠️ Stack

Python
API Notion
Script automatisé (CLI)
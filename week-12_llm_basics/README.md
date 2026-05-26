# Week 12 — LLM Basics: Lead Analyzer

## Objectif

Ce projet introduit l'utilisation d'un LLM dans une automatisation Python.

L'objectif n'est pas de créer un chatbot, mais d'utiliser un modèle IA comme composant d'analyse dans un workflow métier.

## Cas d'usage

Analyse automatique d'un message de lead entrant afin de produire une qualification structurée.

Entrée :

- message libre d'un prospect

Sortie :

- catégorie
- priorité
- score
- niveau de confiance
- résumé
- justification

## Architecture

```text
Lead message
→ PromptBuilder
→ LLMClient
→ OpenAI API
→ JSON response
→ validation
→ decision rule
→ recommended action
Concepts appris
appel d'un LLM via API
utilisation d'une clé API avec .env
séparation entre prompt, client LLM et logique métier
parsing d'une réponse JSON
nettoyage d'une réponse LLM non strictement JSON
validation structurelle
règles de confiance avant action
Fichiers
script.py          # orchestration principale
llm_client.py      # clients LLM : FakeLLMClient / OpenAIClient
prompt_builder.py  # construction du prompt
requirements.txt   # dépendances Python
.env               # clé API locale, non versionnée


## Installation
pip install -r requirements.txt
Configuration

Créer un fichier .env :

OPENAI_API_KEY=your_api_key_here

Ne jamais versionner ce fichier.

Exécution
python script.py
Logique de décision

Le LLM produit une analyse structurée.

Python applique ensuite une règle de confiance :

confidence >= 0.8 + priority High → création automatique d'une tâche
confidence >= 0.6 → validation humaine
sinon → pas de traitement automatique
Point clé

Le LLM ne décide pas seul.

LLM = interprétation
Python = validation + règles + action
Humain = responsabilité sur les cas sensibles

## Limites
le niveau de confiance est estimé par le modèle, pas une vérité statistique
la réponse du LLM peut être mal formatée
l'extraction JSON est simple et pédagogique
pas encore de traitement batch
pas encore d'intégration Make / Notion
```

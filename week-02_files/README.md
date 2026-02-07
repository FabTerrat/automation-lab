# Automatisation de tri de fichiers

## Problème
Des dossiers partagés contiennent des fichiers hétérogènes
(PDF, exports, images, documents) difficilement exploitables
et chronophages à ranger manuellement.

## Solution
Script Python qui :
- analyse un dossier brut
- applique des règles de tri par type de fichier
- crée automatiquement une structure propre
- déplace les fichiers en toute sécurité

## Fonctionnement
- Dossier d’entrée : `input_raw/`
- Dossier de sortie : `output_clean/`
- Tri par extension (.pdf, .csv, .jpg, etc.)

Un mode `DRY_RUN` permet de simuler le tri sans modifier les fichiers.

## Cas d’usage
- Structuration de livrables clients
- Nettoyage de dossiers de reporting
- Organisation d’exports métiers (RH, Ops, Marketing)

## Exécution
```bash
python script.py


Avant exécution réelle, vérifier :
DRY_RUN = False

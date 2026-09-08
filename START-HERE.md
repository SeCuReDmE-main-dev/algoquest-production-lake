# AlgoQuest Production Lake

Ce dépôt coordonne les prompts, images, sources et travaux nécessaires à la transformation d’AlgoQuest en jeu illustré. Il est conçu comme une source de vérité pour humains et agents.

## Produire les dix premières images

1. Ouvrir [`images/incoming/00-base/EX-01/PROMPT.md`](images/incoming/00-base/EX-01/PROMPT.md).
2. Joindre les références énumérées dans le paquet lorsqu’elles sont disponibles.
3. Générer dix fichiers indépendants avec les noms indiqués dans `expected-files.json`.
4. Déposer les fichiers dans `images/incoming/00-base/EX-01/`.
5. Lancer `python tools/import_images.py --packet EX-01 --operator "nom" --producer-tool "outil/version"`.

Les autres lots sont présents pour réserver tous les emplacements. Ils restent bloqués jusqu’à la validation de leur scénario, de leur storyboard et de la direction artistique.

## Commandes

```powershell
python tools/generate_agent_exports.py
python tools/validate_lake.py
python -m mkdocs build --strict
Z:\SecuredMe Education suite\securedme-scholarium\.venv-docs\Scripts\python.exe -m sphinx -W --keep-going -b html sphinx build/sphinx
```

Ne placez aucun secret, renseignement d’apprenant ou donnée privée dans ce dépôt public.

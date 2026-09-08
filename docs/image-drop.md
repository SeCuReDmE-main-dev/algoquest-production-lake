# Déposer et importer les images

Déposez les fichiers dans le dossier `images/incoming` du paquet. Le nom fournit une correspondance candidate ; il ne constitue jamais une approbation.

```powershell
python tools/import_images.py --packet EX-01 --operator "Jean-Sébastien" --producer-tool "GPT Images"
```

L’importeur vérifie le nom, la signature, les dimensions et l’empreinte SHA-256. Il copie les fichiers dans une soumission immuable sans déplacer les originaux. Les noms ambigus comme `image (1).png` restent non associés.

Les décisions `art_reference_selected` et `final_asset_approved` sont indépendantes et exigent une revue humaine.

# TDR-001 — Production lake statique et portable

Statut : accepté le 2026-09-08.

## Décision

Utiliser Git, JSON/JSONL et Markdown comme source canonique ; MkDocs et Sphinx sont deux vues compilées. GitHub Pages publie les données légères. Les originaux approuvés seront distribués par GitHub Releases avec SHA-256.

## Évaluation

| Option | Fitness 35% | Écosystème 20% | Coût 20% | Portabilité/risque 25% | Résultat |
|---|---:|---:|---:|---:|---:|
| Git + fichiers statiques + Pages | 9 | 9 | 10 | 9 | 9.2 |
| Vercel Hobby | 8 | 9 | 8 | 6 | 7.7 |
| Base vectorielle hébergée | 7 | 7 | 3 | 4 | 5.4 |

Les notes sont des évaluations architecturales, pas des benchmarks de performance. Le choix évite un service payant et conserve une copie portable. Vercel Hobby n’est pas retenu comme base d’un projet potentiellement commercial. La base vectorielle reste inutile à 125 sources et 390 slots.

Niveau RagGgE : Tier 1 pour Git/JSON/MkDocs/Sphinx/GitHub Pages ; Tier 3 expérimental pour WebMCP avec repli HTTP ; Tier 4 observer pour une base vectorielle externe.

## Déclencheurs de réévaluation

Réévaluer la recherche sémantique lorsque le catalogue dépasse 10 000 fragments ou lorsque 20 requêtes représentatives ont une précision top-5 inférieure à 80 %. Réévaluer l’hébergement si le site ou les releases approchent leurs limites documentées.

# TDR-003 — Fondation du jeu et dépendances

Statut : accepté le 2026-09-08 pour `GAME-BASE`.

## Décisions

- Conserver React et les contrats AlgoQuest actuels ; créer un reducer de jeu pur et un journal d’événements comme état canonique.
- Utiliser Algorithm Builder comme projection interactive de la fiche et comme producteur de reçus techniques.
- Conserver le moteur narratif interne. Ink et Yarn restent des références jusqu’à ce qu’un POC prouve un bénéfice mesuré.
- Ajouter des adaptateurs séparés pour sauvegarde web, native et synchronisée. Preferences ne contiendra que de petites préférences.
- Garder le rendu DOM/CSS pour la première scène. Évaluer PixiJS uniquement si les mesures montrent que les transitions, le chargement ou le budget mémoire ne peuvent pas être tenus.

## Matrice RagGgE

| Option | Fitness 35 % | Continuité 25 % | Coût 20 % | Risque 20 % | Total |
|---|---:|---:|---:|---:|---:|
| React + moteur actuel + reducer | 9 | 10 | 9 | 9 | 9.3 |
| Migration immédiate vers Ink/Yarn | 8 | 4 | 5 | 5 | 5.8 |
| Nouveau moteur canvas complet | 7 | 3 | 4 | 4 | 4.8 |

Ces notes comparent l’adéquation architecturale observée ; elles ne sont pas des benchmarks. React et le moteur actuel sont Tier 1. Ink/Yarn et PixiJS restent Tier 2, soumis à POC. Une migration complète sans mesure est Tier 4.

## Déclencheurs de réévaluation

- Ink/Yarn : trois histoires ne peuvent pas exprimer leurs reconvergences, ou plus de 20 % de logique particulière par livre.
- PixiJS : la scène cible ne maintient pas 60 images/s au 75e percentile des appareils de test, ou dépasse le budget mémoire défini après les images EX-01.
- Stockage natif : toute perte lors de 100 cycles interruption/reprise bloque la publication mobile.

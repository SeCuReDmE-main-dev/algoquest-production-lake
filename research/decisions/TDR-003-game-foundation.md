# TDR-003 — Fondation du jeu et dépendances

Statut : accepté le 2026-09-08 pour `GAME-BASE`.

## Décisions

- Conserver React et les contrats AlgoQuest actuels ; créer un reducer de jeu pur et un journal d’événements comme état canonique.
- Utiliser Algorithm Builder comme projection interactive de la fiche et comme producteur de reçus techniques.
- Conserver le moteur narratif interne. Ink et Yarn restent des références jusqu’à ce qu’un POC prouve un bénéfice mesuré.
- Ajouter des adaptateurs séparés pour sauvegarde web, native et synchronisée. Preferences ne contiendra que de petites préférences.
- Garder le rendu DOM/CSS pour la première scène. Évaluer PixiJS uniquement si les mesures montrent que les transitions, le chargement ou le budget mémoire ne peuvent pas être tenus.
- Livrer une route immersive `/play` et l’utiliser comme racine de l’application native. Le site public garde ses autres surfaces, mais la partie commence dans un HUD, une scène, une main d’actions et la fiche du héros.
- Compiler Tailwind et les styles dans le paquet. Aucune ressource CDN n’est requise par la route de jeu.
- Utiliser Android Studio AVD, ADB et les tests Playwright comme boucle de contrôle Tier 1. UI Automator 2.4 reste Tier 2 tant que la version étudiée est alpha.

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

## Preuve de réévaluation du 2026-09-08

La première scène DOM/CSS tient dans les vues 390 × 844 et 1440 × 900, sans défilement de page et sans requête externe. Sur l’AVD Android 36 à 1080 × 2400, le même état de partie a été relu après un arrêt forcé et une relance à froid. Son empreinte avant et après est identique. Le choix DOM/CSS et l’adaptateur natif restent donc Tier 1 pour la suite de cette phase.

# GAME-CORE-01 — première passe du moteur et des surfaces

## Objective

Construire une première tranche jouable où AlgoQuest possède l’état canonique et où la même fiche du héros fonctionne dans la planche web, le side panel Algorithm Builder et les enveloppes mobiles.

## Environment and stack

- AlgoQuest : React 19, Vite 6, IndexedDB et Capacitor 8.
- Algorithm Builder : React 19, extension Chrome Manifest V3 et broker Express.
- Contrats : reducer pur, commandes idempotentes, événements, projection de fiche et reçus liés à une partie.
- Environnement : `.env` et `.venv` partagés à la racine de la suite; seules les variables `VITE_` peuvent atteindre le bundle web.

## Questions

1. Quelle couche possède la progression et la mission ?
2. Comment éviter trois fiches divergentes entre web, extension et mobile ?
3. Comment reprendre une partie sans dupliquer une récompense après interruption ?
4. Comment accepter une preuve Builder ou Colab sans faire confiance au navigateur ?

## Findings

### Confirmed by repository contracts and executed tests

- AlgoQuest reste l’autorité. Le Builder manipule une mission liée à la partie et produit un artefact ou un reçu.
- Le paquet versionné `@securedme/hero-sheet` 1.0.2 rend la même projection dans les trois surfaces et conserve la dernière fiche lisible lorsque l’onglet AlgoQuest est fermé.
- La banque contient 40 activités; un parcours construit contient 15 activités obligatoires et 5 optionnelles compatibles avec leurs prérequis.
- Les aides et erreurs gardent l’activité courante. Une commande rejouée avec le même identifiant ne répète pas la récompense.
- IndexedDB groupe état et événements dans une transaction. Un schéma incompatible arrête la reprise avec une erreur explicite et reste intact pour une migration versionnée. Le stockage mobile par générations survit à la corruption de l’état, du journal ou du marqueur de commit, aux interruptions simulées et à 100 cycles sauvegarde/reprise. Capacitor Preferences ne conserve que l’identifiant de la partie active.
- Une suite de parité applique les mêmes commandes aux hôtes mémoire/web et natif et obtient le même état canonique et la même projection de fiche.
- Le service worker lie un canal à l’onglet, au document, à l’origine et à la partie. Sa boîte d’envoi rejoue le même identifiant après redémarrage ou réponse perdue et n’accorde donc pas deux fois une récompense. Les reçus externes sont vérifiés par HMAC côté broker avant admission.

### Confirmed by primary Capacitor documentation reviewed on 2026-09-08

- Une application Capacitor peut intégrer un projet web existant et générer des projets Android et iOS séparés.
- Le plugin Filesystem fournit un stockage natif avec des répertoires contrôlés par la plateforme.
- La compilation et l’exécution natives restent des étapes propres aux chaînes Android Studio et Xcode.

### Measured limitations

- Les suites complètes AlgoQuest et Algorithm Builder passent, leurs audits npm rapportent zéro vulnérabilité connue au moment de cette passe, et MkDocs/Sphinx compilent le registre mis à jour.
- Les parcours Playwright réels couvrent desktop, tablette, mobile tactile et Chromebook simulé. Un second parcours charge l’extension MV3 dans Chromium à 390 px, commande la planche depuis la fiche, ferme l’onglet, vérifie la fiche hors ligne, rouvre AlgoQuest et confirme la reconnexion ainsi que la conservation du brouillon.
- `cap sync` réussit pour Android et iOS sur ce poste.
- Les outils Android officiels ont été téléchargés et leur SHA-256 vérifié. Après acceptation des licences par le propriétaire du poste, `npm run mobile:android:verify` compile l’APK avec Platform 36 et Build-Tools 35. L’APK debug vérifié fait 5 448 444 octets et porte le SHA-256 `43d64b6beb0ca8573da85f6c24b9d8c2b6d27ced4082ffcdbbbe0454767c7cdb`.
- L’APK a été installé et ouvert sur un Galaxy A07. Le propriétaire a confirmé le chargement et le fonctionnement des liens de base, puis a jugé que la présentation n’avait pas encore la qualité ludique recherchée. Le protocole complet de reprise reste à exécuter sur l’appareil; il est versionné dans `docs/android-device-proof.md`. Le projet iOS ne peut pas être compilé sous Windows; il doit être ouvert sur macOS avec Xcode.
- Le broker WebAuth distant, le round-trip Colab distant et l’approbation par des enseignants ou apprenants restent des bloqueurs d’alpha déclarés par le gate.

## Recommended decision

Conserver le reducer AlgoQuest et la projection partagée comme fondation de `GAME-BASE`. Accepter les sous-travaux moteur, fiche, pont et planche sur leurs tests. Garder `MOBILE-01` et `GAME-CORE-01` au statut `submitted` jusqu’au protocole Android complet et à la compilation iOS sur macOS.

## Alternatives considered

- Trois implémentations de fiche séparées : rejetées parce qu’elles multiplient les divergences de comportement et d’accessibilité.
- État détenu par l’extension : rejeté parce que la progression deviendrait dépendante d’un outil auxiliaire.
- IndexedDB comme seule sauvegarde mobile : rejeté au profit d’un adaptateur Filesystem avec générations validées.
- Migration immédiate vers Ink, Yarn ou un moteur canvas : reportée selon les déclencheurs de TDR-003.

## Risks and re-evaluation conditions

- Revoir le modèle narratif si trois histoires ne peuvent pas exprimer leurs reconvergences ou si plus de 20 % de leur logique devient particulière.
- Bloquer la publication mobile si un cycle d’interruption/reprise perd un état ou double une récompense.
- Revoir le rendu si les scènes illustrées finales ne respectent pas les budgets de fluidité et de mémoire après intégration des assets.
- Maintenir une revue humaine avant tout statut alpha ou usage avec des apprenants.

## Sources

- Capacitor, Getting Started: https://capacitorjs.com/docs/getting-started
- Capacitor, Filesystem API: https://capacitorjs.com/docs/apis/filesystem
- Capacitor, Development Workflow: https://capacitorjs.com/docs/basics/workflow
- Décision locale : `research/decisions/TDR-003-game-foundation.md`

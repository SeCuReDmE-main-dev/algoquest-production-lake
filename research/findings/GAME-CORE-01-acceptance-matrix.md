# GAME-CORE-01 — matrice d’acceptation

| Exigence | État | Preuve autoritative | Reliquat |
|---|---|---|---|
| Banque de 40, parcours figé de 20, prérequis, aide/correction stable, récompense unique | Passé | `game-engine-contract-test.mjs` et `gameEngine.js` | Aucun pour cette passe. |
| Une autorité AlgoQuest et même résultat web/native | Passé | `game-host-parity-test.mjs` | Aucun pour les adaptateurs locaux. |
| Planche et fiche agissant sur la même mission | Passé | `game-shell-browser-test.mjs` et `hero-books-browser-test.mjs` | Les images finales remplaceront progressivement la scène procédurale. |
| Extension réelle, panneau étroit, commande, fermeture, reconnexion, brouillon | Passé | `builder-extension-browser-test.mjs` | Aucun pour le transport local. |
| Deux onglets/missions, réponse perdue, worker redémarré, déduplication | Passé | `extension-routing-test.js` et `game-command-outbox-test.js` | Aucun pour le transport local. |
| Reçus liés au propriétaire, partie, affectation, tentative, artefact et signature | Passé en broker de test | `broker-test.js` et `receipt-authentication-test.js` | Broker distant non configuré. |
| Sauvegardes interrompues/corrompues, schéma incompatible, 100 reprises | Passé | `native-game-storage-test.mjs` et `research/evidence/GAME-CORE-01-android-runtime.json` | Aucun pour Android dans cette passe. |
| Mobile tactile, retour sans perte | Passé en navigateur étroit et sur AVD Android | `game-shell-browser-test.mjs` et preuve Android : même état SHA-256 avant/après arrêt forcé | Refaire sur les appareils physiques cibles avant alpha. |
| APK Android compilé, vérifié, installé, joué et relancé | Passé | `research/evidence/GAME-CORE-01-android-build.json`, `GAME-CORE-01-android-runtime.json` et captures associées | Aucun pour cette passe. |
| iOS natif | Non vérifiable sur cet hôte | Projet Capacitor synchronisé | Compilation Xcode sur macOS. |
| Secrets et données d’apprenants exclus | Passé localement | scans, contrôle des variables publiques, audits npm | À répéter avant publication. |

`MOBILE-01` et le parent `GAME-CORE-01` sont acceptés pour la première passe. L’AVD a conservé, octet pour octet, la partie après choix, simulation, arrêt forcé et relance à froid. La compilation iOS demeure une preuve de plateforme distincte et ne doit pas être simulée sous Windows.

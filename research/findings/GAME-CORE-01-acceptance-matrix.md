# GAME-CORE-01 — matrice d’acceptation

| Exigence | État | Preuve autoritative | Reliquat |
|---|---|---|---|
| Banque de 40, parcours figé de 20, prérequis, aide/correction stable, récompense unique | Passé | `game-engine-contract-test.mjs` et `gameEngine.js` | Aucun pour cette passe. |
| Une autorité AlgoQuest et même résultat web/native | Passé | `game-host-parity-test.mjs` | Aucun pour les adaptateurs locaux. |
| Planche et fiche agissant sur la même mission | Passé | `hero-books-browser-test.mjs` | Revue artistique après EX-01. |
| Extension réelle, panneau étroit, commande, fermeture, reconnexion, brouillon | Passé | `builder-extension-browser-test.mjs` | Aucun pour le transport local. |
| Deux onglets/missions, réponse perdue, worker redémarré, déduplication | Passé | `extension-routing-test.js` et `game-command-outbox-test.js` | Aucun pour le transport local. |
| Reçus liés au propriétaire, partie, affectation, tentative, artefact et signature | Passé en broker de test | `broker-test.js` et `receipt-authentication-test.js` | Broker distant non configuré. |
| Sauvegardes interrompues/corrompues, schéma incompatible, 100 reprises | Passé en adaptateur natif simulé | `native-game-storage-test.mjs` | Parcours d’interruption sur appareil. |
| Mobile tactile, retour sans perte | Passé en navigateur mobile simulé; ouverture physique confirmée | `hero-books-browser-test.mjs` et essai propriétaire sur Galaxy A07 | Protocole complet d’interruption/reprise sur l’appareil. |
| APK Android compilé, vérifié, installé et ouvert | Passé | `research/evidence/GAME-CORE-01-android-build.json` et essai propriétaire sur Galaxy A07 | Parcours physique complet. |
| iOS natif | Non vérifiable sur cet hôte | Projet Capacitor synchronisé | Compilation Xcode sur macOS. |
| Secrets et données d’apprenants exclus | Passé localement | scans, contrôle des variables publiques, audits npm | À répéter avant publication. |

`MOBILE-01` et le parent `GAME-CORE-01` restent `submitted` jusqu’au protocole Android complet. La compilation iOS demeure une preuve de plateforme distincte et ne doit pas être simulée sous Windows.

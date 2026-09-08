# Travaux et dépendances

La source canonique est [`jobs/definitions/jobs.json`](https://github.com/SeCuReDmE-main-dev/algoquest-production-lake/blob/main/jobs/definitions/jobs.json). Seul un travail accepté satisfait une dépendance.

Le chemin critique est :

```text
LAKE-02 ──> ART-BASE-01 ───────────────┐
RES-01 ──> RES-02 ──> STORY/ADAPT ──> GAME-BASE ──> GAME-SYSTEMS ──> GAME-CONTENT ──> GAME-FINISH
                         └──> BOARD ──> ART───────────────┘
```

La première passe de code est enregistrée sous `GAME-CORE-01`. `CORE-01`, `SHEET-01`, `BRIDGE-01` et `PLAY-01` sont acceptés sur preuves locales. `MOBILE-01` reste soumis : les sources Android/iOS, la synchronisation Capacitor et 100 cycles de reprise sont validés, tandis que la compilation APK attend un SDK Android et la compilation iOS attend macOS/Xcode.

```text
RES-02 ──> CORE-01 ──> SHEET-01 ──> PLAY-01 ──┐
                    └─> BRIDGE-01              ├─> GAME-CORE-01 ──> GAME-BASE
                       SHEET-01 ──> MOBILE-01 ──┘
```

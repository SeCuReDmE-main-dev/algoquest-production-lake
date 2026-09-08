# Travaux et dépendances

La source canonique est [`jobs/definitions/jobs.json`](https://github.com/SeCuReDmE-main-dev/algoquest-production-lake/blob/main/jobs/definitions/jobs.json). Seul un travail accepté satisfait une dépendance.

Le chemin critique est :

```text
LAKE-02 ──> ART-BASE-01 ───────────────┐
RES-01 ──> RES-02 ──> STORY/ADAPT ──> GAME-BASE ──> GAME-SYSTEMS ──> GAME-CONTENT ──> GAME-FINISH
                         └──> BOARD ──> ART───────────────┘
```

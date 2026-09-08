from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOKS = [
    ("MAG", "mage-two-horizons", "Le Mage des Deux Horizons"),
    ("RON", "ronin-six-provinces", "Le Ronin des Six Provinces"),
    ("MAR", "crown-of-tides", "La Couronne des Marées"),
    ("ALC", "alchemist-oak-gate", "L’Alchimiste et la Porte du Chêne"),
    ("NEU", "neuron-without-brain", "Le Neurone Sans Cerveau"),
    ("CIT", "algorithm-citadel", "La Citadelle des Algorithmes"),
]

MASTER = """Crée une série cohérente de dix images indépendantes pour AlgoQuest, une collection originale de livres interactifs dont le joueur est le héros.

La qualité recherchée est celle d’un jeu illustré avec une direction artistique travaillée : peinture numérique aux matières visibles, compositions soignées, silhouettes lisibles, lumière expressive, détails choisis et cohérence des matériaux. L’univers doit donner envie d’explorer, apprendre, expérimenter et développer son personnage. Il doit convenir aux jeunes et aux adultes sans traitement infantilisant.

Respecte les références approuvées jointes au paquet. Dawncaster, Mythgard et les autres jeux étudiés servent à comprendre la lisibilité, le développement du héros et les interactions ; crée une identité graphique originale pour AlgoQuest.

Produis dix fichiers distincts. Les noms des fichiers et tes commentaires restent à l’extérieur des images. Les couvertures sont sans titre intégré. Les maquettes réservent les espaces du texte et des valeurs qui seront affichés par le code.

Dans les maquettes, Algorithm Builder constitue le panneau interactif permanent : personnage, progression, équipement, actions disponibles, mission active, espace d’expérimentation et échange avec Qbit. La page du livre et ce panneau forment une même expérience de jeu.

Pour Qbit, conserve l’identité des références fournies. N’invente pas un remplacement.

Si ton outil produit moins de dix fichiers par réponse, continue avec les identifiants restants, sans recommencer les images déjà produites.
"""

EX_COMMANDS = [
    ("Mage des Deux Horizons", "couverture conceptuelle verticale : apprenti devant un observatoire ouvert sur deux horizons célestes, instruments de laiton, bleu nocturne, lumière chaude et sensation de découverte. Les phénomènes illustrés restent des métaphores visuelles."),
    ("Ronin des Six Provinces", "couverture conceptuelle verticale : voyageur observant plusieurs routes à travers des provinces contrastées, indigo, vermillon, matière du papier et paysage ample. Faire sentir le choix d’un chemin et ses conséquences."),
    ("Couronne des Marées", "couverture conceptuelle verticale : aventure maritime, navire et archipel, turquoise profond, corail et cuivre. Faire sentir navigation, ressources limitées et incertitude."),
    ("Alchimiste et Porte du Chêne", "couverture conceptuelle verticale : atelier de transformation devant une porte monumentale de chêne, ambre, ivoire et vert mousse, instruments artisanaux et étapes de transformation visibles."),
    ("Neurone Sans Cerveau", "couverture conceptuelle verticale : exploration poétique d’un microcosme de lumière et de particules, violet, cyan et nacre ; un monde à observer et comprendre, sans faux diagramme scientifique."),
    ("Citadelle des Algorithmes", "couverture conceptuelle verticale : architecture de pierre et mécanismes transformables, cobalt et ocre, passages, portes et structures dont on comprend visuellement les relations."),
    ("Livre sur ordinateur", "maquette panoramique : scène illustrée dominante, lecture confortable, choix clairement accessibles et panneau Algorithm Builder intégré à droite. Montrer une aventure en cours avec une hiérarchie visuelle précise."),
    ("Livre sur téléphone", "maquette verticale : illustration, narration, action principale et accès évident au personnage et à la mission. Composer spécifiquement pour le petit écran."),
    ("Panneau — personnage", "maquette verticale : portrait, identité, progression, talents, équipement et historique. Exprimer un personnage qui se développe et dont les choix ont laissé des traces."),
    ("Panneau — mission et Qbit", "maquette verticale : objectif actif, actions manipulables, zone de construction ou d’essai, résultat observable et aide de Qbit. Conserver la même famille graphique que la fiche du héros."),
]

GROUP_META = {
    "G": ("game-narrative-learning", "Dawncaster, gamebooks, narrative authoring and learning research"),
    "X": ("game-reference-assets", "Mythgard, comparable games, hero presentation and asset pipelines"),
    "R": ("runtime-mobile-storage", "React, side panel, mobile, saves and offline runtime"),
    "D": ("quality-accessibility-security", "integrity, testing, accessibility, localization and security"),
    "L": ("production-lake", "documentation, GitHub publishing, WebMCP, provenance and agent access"),
}

URLS = {
"G": """https://wanderlost.games/weekly-challenge-and-an-update-to-progress-rewards/
https://wanderlost.games/synthesis-is-here/
https://wanderlost.games/dawncaster-on-the-big-screen/
https://dawncaster.wanderlost.games/press-release/
https://store.steampowered.com/app/3966890/Dawncaster__The_RPG_Cardventure/
https://www.inklestudios.com/sorcery/
https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md
https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md
https://www.inklestudios.com/ink/web-tutorial/
https://www.inklestudios.com/ink/
https://github.com/inkle/ink/blob/master/Documentation/ArchitectureAndDevOverview.md
https://docs.yarnspinner.dev/3.1/write-yarn-scripts/scripting-fundamentals/options
https://docs.yarnspinner.dev/3.1/write-yarn-scripts/scripting-fundamentals/lines-nodes-and-options
https://docs.yarnspinner.dev/3.1/write-yarn-scripts/scripting-fundamentals/logic-and-variables
https://docs.yarnspinner.dev/3.1/write-yarn-scripts/advanced-scripting/saliency
https://docs.yarnspinner.dev/3.1/write-yarn-scripts/advanced-scripting/storylets-and-saliency-a-primer
https://docs.yarnspinner.dev/components/dialogue-runner
https://pmc.ncbi.nlm.nih.gov/articles/PMC4748544/
https://link.springer.com/article/10.1186/s40594-023-00424-9
https://link.springer.com/article/10.1007/s11423-023-10337-7
https://link.springer.com/article/10.1007/s10648-019-09498-w
https://www.cs.cmu.edu/~bmclaren/pubs/NajarMitrovicMcLaren-LearningWithITSAndWorkedExamples-UMUAI2016.pdf
https://www.ijcai.org/Proceedings/15/Papers/614.pdf
https://doi.org/10.1016/j.learninstruc.2025.102196
https://doi.org/10.1007/s10648-025-10103-6""",
"X": """https://store.steampowered.com/app/839910/Mythgard/
https://rhinogamesinc.itch.io/mythgard
https://www.megacrit.com/press-kits/slay-the-spire/
https://www.gdcvault.com/play/1026309/-Slay-the-Spire-Metrics
https://blog.playstation.com/2021/05/28/weaving-replayable-tales-in-the-griftlands-out-on-ps4-june-4/
https://forums.kleientertainment.com/game-updates/griftlands/451525-r1442/
https://store.steampowered.com/app/601840/Griftlands/
https://www.fellowtraveller.games/citizen-sleeper
https://www.fellowtravellerpresskit.com/citizen-sleeper
https://wildermyth.com/wiki/Hero
https://wildermyth.com/wiki/Writer's_Guide
https://wildermyth.com/wiki/Story_Inputs_and_Outputs
https://wildermyth.com/guide/
https://wanderlost.games/dawncaster-coming-to-steam/
https://megacrit.com/news/2026-8-14-neowsletter-issue-25/
https://pixijs.io/assetpack/docs/guide/pipes/texture-packer/
https://pixijs.download/v8.18.0/docs/assets.Spritesheet.html
https://pixijs.com/8.x/guides/components/assets
https://github.com/goldfire/howler.js
https://sharp.pixelplumbing.com/api-output/
https://sharp.pixelplumbing.com/api-resize/
https://sharp.pixelplumbing.com/api-composite/
https://www.aseprite.org/docs/exporting/
https://www.aseprite.org/docs/sprite-sheet/
https://www.aseprite.org/docs/cli/""",
"R": """https://react.dev/reference/react/useSyncExternalStore
https://react.dev/learn/preserving-and-resetting-state
https://react.dev/learn/choosing-the-state-structure
https://react.dev/reference/react/useReducer
https://capacitorjs.com/docs/basics/workflow
https://capacitorjs.com/docs/getting-started
https://capacitorjs.com/docs/getting-started/environment-setup
https://capacitorjs.com/docs/updating/8-0
https://capacitorjs.com/docs/apis/app
https://capacitorjs.com/docs/apis/preferences
https://capacitorjs.com/docs/apis/network
https://capacitorjs.com/docs/guides/storage
https://capacitorjs.com/docs/apis/filesystem
https://developer.chrome.com/docs/extensions/reference/api/sidePanel
https://developer.chrome.com/docs/extensions/develop/ui/create-a-side-panel
https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
https://developer.mozilla.org/en-US/docs/Web/API/IDBDatabase/transaction
https://developer.mozilla.org/en-US/docs/Web/API/IDBTransaction
https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB
https://web.dev/learn/pwa/offline-data
https://web.dev/learn/pwa/assets-and-data
https://web.dev/learn/pwa/caching
https://web.dev/learn/pwa/update
https://web.dev/articles/storage-for-the-web""",
"D": """https://www.postgresql.org/docs/current/transaction-iso.html
https://www.postgresql.org/docs/current/sql-insert.html
https://www.postgresql.org/docs/18/applevel-consistency.html
https://www.postgresql.org/docs/current/ddl-constraints.html
https://www.postgresql.org/docs/18/explicit-locking.html
https://json-schema.org/understanding-json-schema/reference/array
https://json-schema.org/draft/2020-12/json-schema-validation
https://playwright.dev/docs/locators
https://playwright.dev/docs/accessibility-testing
https://playwright.dev/docs/test-assertions
https://fast-check.dev/docs/advanced/model-based-testing/
https://fast-check.dev/docs/core-blocks/properties/
https://fast-check.dev/docs/api/interfaces/ICommand/
https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
https://www.w3.org/WAI/WCAG22/Understanding/focus-visible
https://www.w3.org/WAI/WCAG21/Understanding/reflow.html
https://www.w3.org/WAI/curricula/designer-modules/interaction-design/
https://www.w3.org/TR/WCAG22/
https://www.i18next.com/translation-function/interpolation
https://www.i18next.com/principles/fallback
https://www.i18next.com/translation-function/plurals
https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/AJAX%5FSecurity%5FCheat%5FSheet.html""",
"L": """https://www.mkdocs.org/user-guide/configuration/
https://www.mkdocs.org/user-guide/deploying-your-docs/
https://www.sphinx-doc.org/en/master/man/sphinx-build.html
https://www.sphinx-doc.org/en/master/usage/builders/index.html
https://www.sphinx-doc.org/en/master/usage/markdown.html
https://myst-parser.readthedocs.io/en/stable/configuration.html
https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
https://docs.github.com/en/rest/repos/contents
https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
https://docs.github.com/en/rest/releases/assets
https://vercel.com/docs/plans/hobby
https://vercel.com/docs/limits/fair-use-guidelines
https://webmachinelearning.github.io/webmcp/
https://developer.chrome.com/docs/ai/webmcp/imperative-api
https://developer.chrome.com/docs/ai/webmcp
https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/guides/webmcp/agentic-javascript-tools/guide.md
https://llmstxt.org/index.html
https://jsonlines.org/
https://www.w3.org/TR/prov-overview/
https://www.w3.org/TR/prov-dm/
https://spdx.github.io/spdx-spec/v2.3/other-licensing-information-detected/
https://github.blog/changelog/2025-06-03-releases-now-expose-digests-for-release-assets/""",
}


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def dump(path: str, value: object) -> None:
    write(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def slot(slot_id: str, packet_id: str, usage: str, status: str, index: int) -> dict:
    return {
        "$schema": "../../../schemas/ImageSlot.v1.schema.json",
        "schema": "securedme.education.algoquest.image-slot.v1",
        "slot_id": slot_id,
        "packet_id": packet_id,
        "filename": f"AQ-{slot_id}__v001.png",
        "revision": 1,
        "usage": usage,
        "status": status,
        "language_scope": "shared-fr-en-es",
        "audience_scope": "shared-six-publics",
        "constraints": {"separate_file": True, "embedded_text": False, "original_visual_identity": True},
        "ordinal": index,
    }


def packet_files(packet_id: str, items: list[dict], status: str, dependencies: list[str], prompt: str) -> dict:
    return {
        "schema": "securedme.education.algoquest.prompt-packet.v1",
        "packet_id": packet_id,
        "revision": 1,
        "status": status,
        "expected_count": 10,
        "dependencies": dependencies,
        "master_prompt_ref": "prompts/master/algoquest-art-direction-v1.md",
        "references": [],
        "slots": [item["slot_id"] for item in items],
        "resolved_prompt_sha256": None,
        "prompt": prompt,
    }


def make_packet(packet_id: str, incoming: str, items: list[dict], ready: bool, dependencies: list[str], prompt: str) -> None:
    status = "ready" if ready else "blocked"
    drop = f"# Déposer les images — {packet_id}\n\nÉtat : **{status}**.\n\nDéposez ici uniquement les dix fichiers définis dans `expected-files.json`. Les originaux ne sont jamais écrasés. L’ordre des fichiers ne sert pas à leur affectation.\n"
    if not ready:
        drop += "\nCe lot attend ses dépendances narratives. `PROMPT.md` décrit son périmètre, mais ne doit pas encore être exécuté.\n"
    write(f"{incoming}/DROP-HERE.md", drop)
    write(f"{incoming}/PROMPT.md", prompt)
    dump(f"{incoming}/expected-files.json", {"schema": "securedme.education.algoquest.expected-files.v1", "packet_id": packet_id, "files": items})
    dump(f"{incoming}/packet.json", packet_files(packet_id, items, status, dependencies, prompt))
    write(f"prompts/packets/{packet_id}.md", prompt)


def build() -> None:
    write("prompts/master/algoquest-art-direction-v1.md", "# Direction artistique maître\n\n" + MASTER)
    all_slots: list[dict] = []
    packets: list[dict] = []

    ex_items = [slot(f"EX-{i:03d}", "EX-01", title, "planned", i) for i, (title, _) in enumerate(EX_COMMANDS, 1)]
    ex_prompt = "# EX-01 — Exploration artistique et interfaces\n\n" + MASTER + "\n## Références à joindre\n\nJoindre `references/approved/qbit/qbit-stencil-guide.png` pour toute représentation de Qbit. Les quatre assets sous `references/approved/brand/` fixent la famille de marque ; ils ne doivent pas être recopiés dans les scènes. Vérifier leurs SHA-256 dans `references/manifest.json`.\n\n## Les dix commandes\n\n" + "\n".join(
        f"### AQ-EX-{i:03d}__v001.png — {title}\n\n{command}\n" for i, (title, command) in enumerate(EX_COMMANDS, 1)
    )
    make_packet("EX-01", "images/incoming/00-base/EX-01", ex_items, True, [], ex_prompt)
    reference_paths = [
        "references/approved/qbit/qbit-stencil-guide.png",
        "references/approved/brand/algoquest-tiny-mark.png",
        "references/approved/brand/algoquest-public-banner.png",
        "references/approved/brand/algoquest-logo-lockup.png",
        "references/approved/brand/algoquest-companion-badge.png",
        "references/approved/brand/source-selection.json",
    ]
    reference_records = []
    for relative in reference_paths:
        reference = ROOT / relative
        if reference.is_file():
            reference_records.append({"reference_id": "REF-" + reference.stem.upper().replace("-", "_"), "path": relative, "sha256": file_sha256(reference), "bytes": reference.stat().st_size, "status": "approved-reference"})
    dump("references/manifest.json", {"schema": "securedme.education.algoquest.reference-manifest.v1", "references": reference_records})
    ex_packet_path = ROOT / "images/incoming/00-base/EX-01/packet.json"
    ex_packet = json.loads(ex_packet_path.read_text(encoding="utf-8"))
    ex_packet["references"] = reference_records
    dump("images/incoming/00-base/EX-01/packet.json", ex_packet)
    all_slots.extend(ex_items); packets.append({"packet_id": "EX-01", "status": "ready", "path": "images/incoming/00-base/EX-01"})

    shared_uses = [
        *[f"avatar-{i:02d}" for i in range(1, 11)],
        *[f"qbit-pose-{i:02d}" for i in range(1, 7)],
        "landing", "library", "tutorial", "collection",
    ]
    for batch in range(1, 3):
        packet_id = f"SH-{batch:02d}"
        start = (batch - 1) * 10
        items = [slot(f"SH-{n:03d}", packet_id, shared_uses[n - 1], "blocked", n) for n in range(start + 1, start + 11)]
        prompt = f"# {packet_id} — Assets communs\n\nÉTAT : BLOQUÉ. Ce paquet sera résolu après validation de la direction artistique EX-01 et des références Qbit.\n\nPérimètre : " + ", ".join(x["usage"] for x in items) + ".\n"
        make_packet(packet_id, f"images/incoming/10-shared/{packet_id}", items, False, ["ART-BASE-01"], prompt)
        all_slots.extend(items); packets.append({"packet_id": packet_id, "status": "blocked", "path": f"images/incoming/10-shared/{packet_id}"})

    batch_uses = {
        1: ["cover", "map", "act-opener-1", "act-opener-2", "act-opener-3", "act-opener-4", "act-opener-5", "recurring-place-1", "recurring-place-2", "recurring-place-3"],
        2: [f"playable-scene-{i}" for i in range(1, 11)],
        3: [f"playable-scene-{i}" for i in range(11, 21)],
        4: [f"cast-portrait-expression-{i}" for i in range(1, 11)],
        5: [*[f"tool-equipment-{i}" for i in range(1, 5)], *[f"talent-{i}" for i in range(1, 4)], *[f"quest-object-{i}" for i in range(1, 4)]],
        6: [*[f"changed-state-{i}" for i in range(1, 7)], "branch-scene-1", "branch-scene-2", "conclusion-variation-1", "conclusion-variation-2"],
    }
    for code, slug, title in BOOKS:
        dump(f"content/books/{slug}/book.json", {"schema": "securedme.education.algoquest.production-book.v1", "book_id": slug, "code": code, "title": title, "image_budget": 60, "audiences": ["primary-5-6", "secondary-1-2", "secondary-3-5", "college", "university", "teacher-player"], "locales": ["fr-CA", "en", "es"]})
        for batch in range(1, 7):
            packet_id = f"{code}-B{batch:02d}"
            start = (batch - 1) * 10
            items = [slot(f"{code}-{n:03d}", packet_id, batch_uses[batch][n-start-1], "blocked", n) for n in range(start + 1, start + 11)]
            dependencies = [f"BOARD-{slug}", "ART-BASE-01"]
            prompt = f"# {packet_id} — {title}\n\nÉTAT : BLOQUÉ. Ne pas produire ce lot avant validation de `{dependencies[0]}` et de la direction artistique.\n\nCe lot contiendra : " + ", ".join(x["usage"] for x in items) + ". Le prompt final sera autonome et versionné lorsque le casting, les lieux et les scènes seront approuvés.\n"
            incoming = f"images/incoming/20-books/{slug}/B{batch:02d}"
            make_packet(packet_id, incoming, items, False, dependencies, prompt)
            all_slots.extend(items); packets.append({"packet_id": packet_id, "status": "blocked", "path": incoming})

    dump("content/shared/image-slots.json", {"schema": "securedme.education.algoquest.image-slot-registry.v1", "count": len(all_slots), "slots": all_slots})
    dump("prompts/packets/index.json", {"schema": "securedme.education.algoquest.packet-registry.v1", "count": len(packets), "packets": packets})

    sources = []
    for group, raw in URLS.items():
        topic, description = GROUP_META[group]
        for index, url in enumerate(raw.splitlines(), 1):
            sources.append({
                "schema": "securedme.education.algoquest.research-source.v1",
                "source_id": f"{group}{index:02d}", "url": url, "topic": topic,
                "coverage": description, "retrieval": "exa", "fetch_status": "reviewed-bounded-excerpt",
                "retrieved_on": "2026-09-08", "deep_read_status": "pending", "limitations": ["Bounded excerpt; not a claim of complete-page or full-paper reading."],
            })
    dump("research/sources/catalog.json", {"schema": "securedme.education.algoquest.research-catalog.v1", "total": len(sources), "game_source_count": 100, "lake_source_count": 25, "sources": sources})
    write("research/sources/catalog.jsonl", "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in sources))

    jobs = [
        ("LAKE-01", [], "accepted", "Repository schemas, 39 packets and 390 slots"),
        ("LAKE-02", ["LAKE-01"], "accepted", "Executable EX-01 prompt book"),
        ("LAKE-03", ["LAKE-02"], "running", "Agent exports, docs, WebMCP and publishing"),
        ("ART-BASE-01", ["LAKE-02"], "ready", "Ten exploration submissions and art-direction review"),
        ("RES-01", [], "accepted", "100 game sources and 25 production-lake sources"),
        ("RES-02", ["RES-01"], "running", "Deep synthesis and technology decisions"),
    ]
    for _, slug, _ in BOOKS:
        jobs.extend([
            (f"STORY-{slug}", ["RES-02"], "blocked", "Substantial rewrite of Luna Light draft"),
            (f"ADAPT-{slug}", [f"STORY-{slug}"], "blocked", "Six playable audience adaptations"),
            (f"BOARD-{slug}", [f"STORY-{slug}", f"ADAPT-{slug}"], "blocked", "Approved visual storyboard and casting"),
            (f"ART-{slug}", [f"BOARD-{slug}", "ART-BASE-01"], "blocked", "Six ten-image production batches"),
        ])
    jobs.extend([
        ("GAME-BASE", ["RES-02", "ART-BASE-01"], "blocked", "Playable book shell and Algorithm Builder hero panel"),
        ("GAME-SYSTEMS", ["GAME-BASE"], "blocked", "Progression, missions, saves and tool receipts"),
        ("GAME-CONTENT", ["GAME-SYSTEMS", *[f"ADAPT-{slug}" for _, slug, _ in BOOKS]], "blocked", "Six integrated adventures"),
        ("GAME-FINISH", ["GAME-CONTENT", *[f"ART-{slug}" for _, slug, _ in BOOKS]], "blocked", "Visual finish, accessibility and complete playtests"),
    ])
    job_records = [{"schema": "securedme.education.algoquest.production-job.v1", "job_id": jid, "depends_on": deps, "status": state, "expected_output": output, "revision": 1} for jid, deps, state, output in jobs]
    lake_publish = next(job for job in job_records if job["job_id"] == "LAKE-03")
    lake_publish["status"] = "accepted"
    lake_publish["evidence"] = [
        "https://github.com/SeCuReDmE-main-dev/algoquest-production-lake/actions/runs/34250834687",
        "https://securedme-main-dev.github.io/algoquest-production-lake/",
        "https://securedme-main-dev.github.io/algoquest-production-lake/agent/index.json",
        "https://securedme-main-dev.github.io/algoquest-production-lake/reference/",
    ]
    dump("jobs/definitions/jobs.json", {"schema": "securedme.education.algoquest.job-registry.v1", "jobs": job_records})
    write("jobs/events/events.jsonl", "".join(json.dumps({"schema": "securedme.education.algoquest.job-event.v1", "job_id": j["job_id"], "event": "status-set", "status": j["status"], "at": "2026-09-08T00:00:00-04:00", "actor": "codex-coordinator"}, ensure_ascii=False) + "\n" for j in job_records))

    write("research/findings/initial-synthesis.md", """# Synthèse initiale de conception

Statut : synthèse de premier passage fondée sur 100 extraits bornés. Une lecture profonde ciblée reste requise avant `GAME-BASE`.

## Décisions déjà assez solides

- La progression du héros suit quatre temps : acquis permanents, configuration initiale choisie, développement pendant l’aventure, puis traces durables à la conclusion. Dawncaster documente des déblocages choisis et des options de départ (G01–G04).
- Les six histoires conservent des buts et conclusions écrits, tandis que les sous-intrigues, relations et situations répondent aux décisions. L’approche est cohérente avec Griftlands et Wildermyth (X05, X10–X13).
- Les activités éducatives doivent être des actions du jeu avec une conséquence visible. Les recherches G18–G25 ne permettent pas de prétendre qu’une couche de points rend le jeu efficace.
- Un essai, une aide ou une reprise conserve l’activité attribuée. Les systèmes de conditions et de contenu joué une seule fois offrent des modèles d’auteur, sans imposer Ink ou Yarn (G07–G17).
- Le panneau Algorithm Builder projette l’état canonique d’AlgoQuest et renvoie des reçus techniques ; il ne décide ni de l’activité suivante ni de la récompense.
- Les sauvegardes web et natives auront des adaptateurs séparés. La documentation Capacitor avertit que le stockage WebView peut être récupéré par le système (R10–R13).

## Limites

Les pages commerciales décrivent une intention de produit et ne prouvent pas le plaisir. Les études G22–G25 portent sur des populations et tâches précises ; elles ne valident pas les six publics. Les outils d’assets X16–X25 sont des options à tester, pas des dépendances retenues.
""")
    write("research/decisions/TDR-001-production-lake.md", """# TDR-001 — Production lake statique et portable

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
""")
    write("research/decisions/TDR-002-narrative-runtime.md", """# TDR-002 — Conserver le moteur narratif existant

Statut : accepté sous réserve des tests de `GAME-BASE`.

Ink et Yarn apportent des modèles utiles de branches, variables, reconvergence et séparation auteur/runtime (G07–G17). Ils ne sont pas ajoutés maintenant : AlgoQuest possède déjà ses contrats de missions, preuves et progression. Le coût d’une migration n’a pas encore de bénéfice mesuré.

Déclencheur : réaliser un POC borné seulement si trois scénarios réécrits ne peuvent pas exprimer leurs reconvergences ou si la validation du graphe exige plus de 20 % de logique particulière par livre.
""")


if __name__ == "__main__":
    build()
    print("Scaffold generated: 39 packets, 390 image slots, 125 research sources")

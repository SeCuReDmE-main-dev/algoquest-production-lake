# Accès des agents

`agent/index.json` est le point d’entrée. Il référence les paquets, slots, sources et travaux. `llms.txt` décrit la surface publique.

Le site expose des outils WebMCP de lecture lorsque le navigateur fournit `document.modelContext`. Le repli est un accès HTTP aux mêmes fichiers. WebMCP ne confère aucune autorité d’écriture.

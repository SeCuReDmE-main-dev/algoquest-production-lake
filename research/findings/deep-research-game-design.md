# Recherche approfondie ciblée — fondation du vrai jeu

Statut : acceptée pour débloquer la conception technique. Réalisée le 2026-09-08 avec Exa sur 20 sources déterminantes, jusqu’à 10 000 caractères par source. Il s’agit d’une lecture ciblée ; les articles et documents longs ne sont pas déclarés lus intégralement.

## Conclusion de produit

AlgoQuest doit faire vivre une **aventure tactique écrite**. Le joueur construit un répertoire d’actions, de méthodes, d’outils et de formulations qui jouent le rôle mécanique d’un deck, sans transformer l’expérience en combat de monstres. Chaque action dépense ou transforme une ressource visible, modifie une situation narrative et produit une trace dans la fiche du héros.

Le plaisir recherché vient de quatre boucles liées : choisir une intention, combiner des actions limitées, observer une conséquence claire, puis améliorer le héros. La connaissance scolaire intervient dans la décision ou dans la preuve demandée ; elle ne doit pas apparaître comme un questionnaire interrompant le jeu.

## Développement du héros

Dawncaster décrit le remplacement d’une progression linéaire par une monnaie permettant de choisir sa route de déblocage, puis des pistes qui ouvrent cartes de départ, attaques de base et portraits (G01, G02). Son discours produit lie aussi l’identité du personnage aux choix de construction et aux rencontres (G04). Ces pages décrivent leur jeu ; elles ne prouvent pas que ce mécanisme convient automatiquement aux élèves.

AlgoQuest adopte donc quatre couches distinctes :

1. **Acquis du compte** : options gagnées dans AlgoQuest ou les autres outils autorisés de la suite.
2. **Configuration de départ** : héros, talent initial et petit ensemble d’actions choisis avant l’histoire.
3. **Construction de l’aventure** : nouvelles actions, améliorations et objets choisis pendant la partie.
4. **Héritage** : accomplissements et possibilités durables accordés à la conclusion, jamais pour un simple nombre de clics.

La fiche du héros affiche l’origine de chaque acquis et les décisions qui l’ont transformé. Elle sert aussi de surface d’action avec Qbit et Algorithm Builder.

## Histoire écrite et variabilité

Sorcery montre une carte illustrée et une histoire qui répond aux actions (G06). Ink documente des branches fréquentes, leurs conséquences et leur reconvergence dans un texte révisable (G07). Yarn distingue branches écrites et sélection dynamique de storylets (G16). Klei explique pour Griftlands que les buts supérieurs restent stables pendant que sous-intrigues, rôles de personnages et réactions varient (X05). Wildermyth sélectionne des rôles narratifs à partir de l’état de campagne, des traits et relations (X12).

Pour les six livres, les cinq actes, la finalité pédagogique et la conclusion canonique restent écrits. Les routes, relations, ressources, blessures symboliques, outils et scènes intermédiaires varient. Une branche importante peut reconverger, mais la fiche conserve la trace de ce qui s’est passé. Aucun générateur libre ne remplace le scénario approuvé.

Le moteur existant reste en place. Ink et Yarn deviennent des références de validation : identifiants stables, conditions explicites, fins atteignables, absence de cul-de-sac accidentel et distinction entre texte, choix et commande de jeu.

## Boucle d’une scène

Chaque scène suit le contrat suivant :

```text
Situation illustrée → intention du joueur → actions disponibles
→ construction ou choix dans le panneau → preuve/conséquence
→ modification du monde et du héros → prochaine situation
```

Une main contient des **actions** : observer, questionner Qbit, comparer, simuler, négocier, classer, déboguer, protéger une ressource ou employer un objet. Certaines actions viennent de prompts adaptés au public. Une action utilisée est consommée pour la scène ou le parcours selon son contrat. Les aides et reprises reprennent la même attribution.

Une aventure complète tire 20 activités distinctes dans une banque de 40 : 15 essentielles et 5 admissibles choisies à partir des prérequis, sans redistribution après coup. L’unicité porte sur les identifiants métier et sera vérifiée séparément de JSON Schema.

## Apprentissage et adaptation

Les synthèses G18–G20 indiquent que les effets varient avec les mécanismes, la narration et la qualité de l’étude. Elles incitent à tester séparément apprentissage, autonomie ressentie et comportement. G22 rapporte un avantage pour une sélection adaptative fondée sur les besoins d’assistance dans un contexte de tuteur intelligent ; cette étude ne valide pas les six publics d’AlgoQuest.

L’adaptation utilisera seulement des éléments observables et expliqués : public choisi, prérequis déclarés, réussite de l’action actuelle, demandes d’aide et preuves fournies. Elle pourra changer le vocabulaire, la quantité d’étayage, le nombre d’étapes et les exemples. Elle ne modifiera pas secrètement la personnalité du joueur et ne produira pas de diagnostic.

L’enseignant-joueur possède sa propre aventure : arbitrer des preuves, construire un parcours, aider des personnages et gérer l’incertitude pédagogique. Il ne s’agit pas d’un tableau administratif déguisé.

## Interface, sauvegarde et qualité

React recommande une source d’état sans duplications contradictoires (R03). Le jeu utilisera un reducer pur partagé ; le livre et le panneau en seront deux projections. L’API Chrome Side Panel exige Chrome 114 et `open()` demande une action utilisateur à partir de Chrome 116 (R14). Sur mobile, le panneau devient un écran ou tiroir persistant dans la navigation.

Capacitor avertit que localStorage et IndexedDB d’une WebView iOS peuvent être récupérés et réserve Preferences aux petites valeurs (R12). La sauvegarde du parcours aura donc des adaptateurs web et natif, un journal versionné et une synchronisation de compte séparée. Aucun identifiant de session ne sera stocké comme donnée de jeu ; OWASP demande de traiter le stockage client et `postMessage` comme non fiables (D22).

Les cibles de contrôle respecteront au minimum WCAG 2.2 AA 24 × 24 CSS avec espacement, avec 44 × 44 comme objectif ergonomique du jeu lorsque la disposition le permet (D14). Les contrôles automatisés Playwright/axe seront complétés par clavier, lecteur d’écran, zoom et essais humains (D09). Un fallback i18next ne comptera jamais comme traduction complète (D20).

## Pipeline artistique

Les assets seront organisés par livre et scène, chargés par manifeste et optimisés en dérivés traçables. PixiJS documente les bundles, le préchargement de fond et les fallbacks de formats (X18), mais le simple chargement d’images ne justifie pas encore l’ajout de PixiJS. La première interface doit mesurer les limites du DOM/CSS actuel avant cette décision.

Les images portent l’atmosphère, le personnage et les conséquences. Les chiffres, textes, graphes et états interactifs restent rendus par le code. Le même original peut couvrir plusieurs adaptations seulement par une association explicite.

## Critères avant `GAME-BASE`

- Les dix images EX-01 sont reçues, identifiées et revues ; au moins une direction du livre et une du panneau sont retenues.
- Le reducer peut rejouer une séquence à partir d’un journal et produire le même état.
- Un prototype de scène démontre situation, choix d’actions, preuve, conséquence et progression du héros.
- Le panneau affiche le personnage et permet réellement une mission ou interaction avec Qbit.
- Une sauvegarde interrompue ne duplique ni activité ni récompense.
- Les essais comparent compréhension, friction et envie de rejouer ; aucun score esthétique interne ne sera présenté comme preuve de plaisir.

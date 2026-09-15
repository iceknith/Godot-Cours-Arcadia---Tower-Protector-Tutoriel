Introduction à la programmation
===============================

La programmation est au centre du développement de jeu vidéo.
Ça peut paraître vachement complexe, mais en réalité, c'est plutôt simple.

.. note::
    Cette partie du tutoriel est une sorte de préquel au tutoriel d'apprentissage de Godot.
    Si vous savez déjà ce que sont des variables, types et fonctions, vous pouvez sauter cette partie, sinon vous êtes au bon endroit.

La programmation, c'est quoi ?
-----------------------------

La programmation, c'est l'art de donner des instructions à l'ordinateur. 
L'ordinateur y obéira, et ainsi, vous pouvez faire des calculs, afficher des trucs à l'écran, et au final... faire des jeux.

Vu que les ordinateurs sont des machines extrêmement complexes, il y a **pleins** de "langages de programmation", 
qui ont chacun leurs spécificités propres, ils ont de la façon différente de communiquer avec l'ordinateur, sont plus ou moins efficace, 
mais au fond, les principes que nous allons apprendre ici s'appliquent grossièrement à tous les langages.

Vu que ce tutoriel vous apprend à utiliser Godot, on va apprendre à programmer en `GDScript`, qui est le langage de programmation attitré de Godot.
Mais ça ressemble beaucoup à `Python`, le langage de programmation le plus populaire au monde.

Les variables
-------------

Le concept de variables est le plus important de la programmation.

Les variables sont des sortes de "boites" dans lesquelles on peut mettre des valeurs : un nombre, du texte, une image de chien…

En `GDScript`, on les définit comme ça:

.. code-block:: gdscript

    var nomDeVariable = valeur


Le mot clé `var` nous sert à dire à notre ordinateur qu'on veut définir une variable.

Par exemple, si je veux avoir le résultat de `1 + 1`, je peux faire:

.. code-block:: gdscript

    var deux = 1 + 1

Soi-disant passant, les **opérations mathématiques simples** en `GDScript` sont écrite comme on les écrirai naturellement.
Si vous avez compris ça, vous avez compris le concept le plus important de la programmation.

Les types
---------

Avec les variables, on a définit des petites boites, dans lesquelles on peut stocker des valeurs.
Mais, nos ordinateurs sont très bêtes, et ont besoin que tout soit catégorisé, que tout ait une étiquette de ce qu'il est.

Et c'est ce que sont les types: des **étiquettes**. Ça dit à l'ordinateur ce qu'il y a dans notre boîte.

En `GDScript``, il y en a **beaucoup**, mais ici on va voir les plus communs :
- `int`: Des entiers naturels, comme `1`, `6` ou `9026`.
- `float`: Des nombres à virgules, et qui ont un `.` à la place de la virgule, par exemple : `0.6`, `9.6` ou `100.001`.
- `String`: Du texte, ils doivent commencer et terminer par `"`
- `bool` : Des booléens, ils peuvent contenir 2 valeurs : `true` pour vrai et `false` pour faux.



Les blocs conditionnels
-----------------------

Les boucles
-----------

Les fonctions
-------------

Les listes
----------

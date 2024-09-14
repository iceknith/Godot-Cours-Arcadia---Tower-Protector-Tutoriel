Création du Joueur
========

Dans cette partie du tutoriel, nous allons créer un joueur, lui ajouter des animations, et des mouvements basiques:

.. image:: img/demoPlayer.gif

.. init-joueur:

Initialisation du Joueur
--------

Pour commencer, nous allons créer un ``CharacterBody2D``, c'est un `noeud` en 2d, qui est fait pour créer des personnages avec des mouvements fluides.
En haut à gauche, créez une nouvelle scène en cliquant sur le bouton **Other Node** ou le bouton **+**. Ajoutez un ``CharacterBody2D``.
Le noeud CharacterBody2D devrait apparaître dans l'arborescence, et l'éditeur devrait être passé en mode 2D.
Avant toute chose, sauvegardez votre nouvelle scène en appuyant sur ``Ctrl+S``. Vous pouvez créer un dossier ``scenes`` dans votre projet, et y enregistrer la scène du joueur en l'appellant ``player.tscn``.

À droite du ``CharacterBody2D``, vous devriez apercevoir un icône de warning. Si vous mettez votre souris dessus, vous verrez le message suivant:

.. image:: img/characterbody2dwarning.png

`"Ce nœud n'a pas de forme, il ne peut donc pas entrer en collision ou interagir avec d'autres objets.
Envisagez d'ajouter un ``CollisionShape2D`` ou un ``CollisionPolygon2D`` en tant qu'enfant pour définir sa forme."`

Qu'il en soit ainsi, ajoutons un ``CollisionShape2D`` en cliquant sur l'icône **+** en haut à gauche, en appuyant sur ``Ctrl+A`` ou encore en faisant: **Clic-droit -> Ajouter un nœud** sur le ``CharacterBody2D``.

Le nœud ``CollisionShape2D`` est utilisé pour ajouter des hitbox (aka des boîtes de collision). C'est la chose qui permettra à notre joueur d'interagir physiquement avec le monde autour de lui.
Après avoir ajouté la ``CollisionShape2D``, vous devriez avoir un autre warning disant que la ``CollisionShape2D`` n'a pas de forme.
Pour ajouter une shape, cliquez sur le nœud ``CollisionShape2D``. Vous verrez alors que l'inspecteur, à droite de l'écran, affiche des informations sur la ``CollisionShape2D``.
Ajouter une ``CapsuleShape2D`` dans l'attribut ``shape``, qui est normalement vide. Vous devriez voir un espèce de Tic-Tac bleu au milieu de votre écran, c'est la shape.
Vous pouvez changer sa taille avec les petits cercles oranges, mais on fera ça un tout petit peu plus tard.

.. init-anims:

Création d'animations
--------

À présent, nous avons un joueur constitué d'un ``CharacterBody2D`` et d'une ``CollisionShape2D``. C'est bien, mais ce n'est pas très beau.

Ajoutons donc un sprite à notre joueur. Un sprite, c'est tout simplement une texture 2D, ça qui va gérer les images de joueur affichées sur votre écran.
On veut que notre joueur ait des animations, donc ajoutez un nœud ``AnimatedSprite2D`` au joueur.
Faites attention à ce que le nœud soit un enfant du ``CharacterBody2D``, et non de la ``CollisionShape2D``. En effet, on ne veut pas ajouter un sprite à notre collision, on veut ajouter un sprite à notre joueur.
Si le nœud est mal placé dans l'arborescence, vous pouvez le drag-n-drop (restez appuyé sur le nœud et glissez-le) sur le nœud joueur.
Vous pouvez aussi renommer le nœud du joueur en ``Player``. Après ça, vous devriez avoir une arborescence comme ça:

.. image:: img/playerscene.png

Encore un warning! Cette fois-ci sur l'``AnimatedSprite2D``. Ajoutez donc un ``SpriteFrames``, comme le recommande le warning.

.. rappel::
   Pour ajouter un nouveau ``SpriteFrames``, cliquez d'abord sur l'``AnimatedSprite2D`` dans l'arborescence.
   Vous aurez alors accès aux propriétés du nœud dans l'inspecteur, qui se trouve à droite de votre fenêtre.

Après avoir ajouté un nouveau ``SpriteFrames``, une nouvelle fenêtre devrait apparaître en bas de votre écran.
Si ce n'est pas le cas, cliquez sur le ``SpriteFrames`` que vous venez de créer dans l'inspecteur.

.. image:: img/spriteframesopened.png

Cette fenêtre est l'éditeur d'animations. Vous pouvez le fermer et le réouvrir en cliquant sur `SpriteFrames` en bas de l'écran.
À gauche, vous trouverez une liste de toutes les animations disponibles. Pour l'instant, il n'y en a qu'une, elle s'appelle ``"default"``.
Renommez-la ``"idle"``.

.. note::
   Une animation d'idle, c'est l'animation qui se joue quand le personnage ne bouge pas.
   Généralement, elle représente le personnage qui respire, pour ajouter du mouvement à l'image et pour faire vivre le jeu.
   Dans certains jeux, si vous attendez suffisamment longtemps, des animations spéciales vont se jouer: le personnage qui se gratte la tête, ou qui s'asseoit par terre ou s'endort...

Cliquez ensuite sur l'icône de grille: `Add frames from sprite sheet`, et ouvrez le fichier ``assets/player.png``.

.. note::
   Une ``spritesheet`` est un fichier image qui contient toutes les frame d'animation d'un objet.
   Celà permet de n'avoir qu'un fichier, au lieu de plusieurs, ce qui économise de la place
   Mais, du coup, pour avoir les frame d'animation, il faut les extraire depuis la spritesheet, en utilisant un ``spritesheet Cutter``

Celà vous ouvrira le Spritesheet Cutter, qui ressemblera à ça:

.. image:: img/spritesheetCutter.png

Vous pouvez alors mettre le nombre de frames par colones `[1]` et le nombre de frames par lignes `[2]`.
Si la grille des frames est alignée avec celle proposée par le `spritesheet cutter`,
alors vous pouvez séléctionner les 6 premières frames (toutes les frames de la première ligne), en cliquant dessus.
Finalement, vous pouvez appuyer sur `Add 6 Frames`, pour ajouter les frames à votre animation d'idle.

.. image:: img/spriteframesIdle.png

Maintenant, vous pouvez jouer l'animation, en appuyant sur `play` `[1]`,
et changer la vitesse de l'animation, en changeant ses `FPS` (Frames Per Second) `[2]`

Une animation d'`idle` c'est bien, mais, nous aimerions que notre joueur puisse bouger,
donc on va rajouter une animation de course, qu'on appellera ``run``

Pour celà, appuyez sur `Add Animation`, en haut à gauche de la fenêtre `SpriteFrames`.
Renommez, votre animation en ``run``, et répétez les mêmes étapes que pour l'animation d'idle,
mais au lieu de sélectionner les 6 premières frames du spritesheet,
il faudra sélectionner les 6 frames d'après (toutes les frames de la deuxième ligne)

.. move-init:

Création des mouvements
--------

Actuellement nous avons un joueur, qui as des animations, mais qui ne fait pas grand chose.
Dans cette partie, nous allons lui ajouter des mouvements rudimentaires.

[temp :]

- création gdScript "vide" (pas le truc prédéfini)
- tutoriel rapide sur la syntaxe gdscript
- explication ``_physic_process(delta)`` (avec schéma)
- parler de faire Input.get_axis("ui_left", "ui_right") -> velocity.x = direction * 300
- mettre direction dans un vect2


.. anims-fin:

Animation du personage
--------

Actuellement, notre personage bouge, mais il reste toujours dans le même animation,
alors qu'on veut qu'il change d'animation dynamiquement

[temp:]

- lancement de l'animation par défaut
- changement de l'animation selon si on avance ou pas
- changement de l'orientation de l'animation


.. move-fin:

Peaufinage des mouvements
--------

Actuellement, nous avons un système de mouvement qui fonctionne,
mais qui n'est pas très agréable à utiliser, alors on va l'ameillorer


[temp :]
- normalisation vect ``direction``
- ajout inertie:``lerp``
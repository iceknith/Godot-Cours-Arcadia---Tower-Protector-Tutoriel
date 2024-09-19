

[temp]

- Création sommaire de la tour (nodes, sprite)
- Création du script de la tour






Création de la tour
===================

Initialisation de la tour
-------------------------

Pour l'instant, on a donc un monde avec un petit joueur qui peut se déplacer dedans.
Cependant, le joueur n'a pas grand chose à faire puisqu'il est tout seul dans ce petit monde.

Si on reprend le gif de présentation:

.. image:: img/preview.gif

Dans cette partie, on va créer la tour au milieu du monde.
Pour ce faire, vous aurez besoin de créer une nouvelle scène, qui soit un ``StaticBody2D``.

.. note::
    Les nœuds ``StaticBody2D`` sont utilisés pour représenter des objets solides (avec lesquels on veut collider) et immobiles.
    Concrètement, c'est très utile pour les murs, les sols, etc.
    Ici, la tour est immobile, et on ne veut pas que le joueur puisse la traverser, donc un ``StaticBody2D`` est parfait.

Comme pour notre player, il faut lui rajouter une ``CollisionShape2D`` et un ``AnimatedSprite2D``.

Rajoutez un ``SpriteFrames`` à l'``AnimatedSprite2D`` dans l'Inspecteur.
Ajoutez deux animations: ``"alive"`` et ``"dead"``.
Dans notre jeu, la tour a deux états: elle est vivante la majorité du temps, et elle est morte lorsque suffisamment d'ennemis l'ont touchée.
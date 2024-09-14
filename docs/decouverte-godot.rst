Découverte de Godot
=========

Installation de Godot
------------

Pour commencer le tutoriel, il vous faudra installer Godot. Pour celà, vous pouvez aller sur `ce site <https://godotengine.org/download/>`_ , pour y télécharger la dernière version de Godot.


Une fois le fichier .zip téléchargé et dézippé, vous pouvez lancer l’installeur, et après un peu d’attente, vous pourrez lancer godot, et être accueilli par cette fenêtre:


.. image:: img/projectmanager.png


Création de votre premier projet
------------

Cette fenêtre s'appelle le `Project Manager`. C'est ici que vous trouverez vos différents projets une fois que vous les aurez créés.
Actuellement, le `Project Manager` est vide, donc créons notre premier projet.

.. note::
   Pour ce tutoriel, les screenshots et les termes que nous utiliserons seront en anglais.
   C'est généralement un meilleur choix de tout mettre en anglais lorsqu'on programme, et la documentation sur internet est plus fournie en anglais qu'en français.
   Libre à vous bien sûr de mettre votre éditeur dans la langue de votre choix, mais il se peut que certains boutons n'aient pas les mêmes libellés chez vous.
   Vous pouvez changer la langue de l'éditeur dans les `Paramètres` en haut à droite du `Project Manager`, ou dans `Editor Settings` dans l'éditeur.

Cliquer sur le bouton **New** en haut à gauche.
Un popup s’ouvrira, en vous demandant des informations sur votre projet. Pour l'instant, vous n'avez qu'à nommer votre projet (1), et à choisir le fichier dans lequel vous voulez qu’il soit stocké (2).

.. image:: img/newproject.png

Laissez les autres paramètres comme ils sont pour l'instant, et créez votre projet. Une nouvelle fenêtre devrait se lancer.
C'est la fenêtre principale de Godot, l'éditeur, celle où vous aller tout faire sur vos jeux.

L'éditeur
------------

Dans cette sous-partie, nous allons décrire les différents éléments qui composent l'éditeur:

.. image:: img/editor.png

1. Au milieu, vous trouverez la fenêtre principale de l'éditeur, celle-ci vous permettera de pré-visionner, et de modifier graphiquement l'élément ouvert de votre projet.
2. En bas à gauche, vous trouverez l'arborescence. Il s'agit en réalité du dossier que vous venez de créer en créant le projet. Vous pouvez le retrouver sur votre ordinateur en suivant le chemin de votre projet (que vous avez rempli plus tôt).
3. Juste au dessus, en haut à gauche, on trouve l'arborescence des scènes. Godot fonctionne d'une manière arborescente, c'est à dire que chaque élément, chaque personnage, etc... est un `noeud`, qui est le fils d'un autre `noeud`, et qui peut avoir des enfants. Ce fonctionnement est extrêmement puissant, et fait en sorte que, par exemple, un joueur n'est pas fonctionnellement différent d'un environnement.
4. A droite, on peut voir l'éditeur, c'est la partie de l'éditeur qui va vous permettre de modifier les différents paramètres du `noeud` actuel.
5. Et en bas, vous trouverez le reste des éditeurs. Tout ce qui n'est pas dans les 4 autres points est en bas. Celà inclut par exemple, la fenêtre de débug, l'éditeur d'annimation, et l'éditeur de tilemaps.


Importer les assets
--------------

Après avoir crée le projet, il nous faut installer les différents `assets`

.. note::
   `asset` est le nom donné aux éléments non-code d'un jeu vidéo, par exemple, une texture, un font ou une musique.

Pour celà, téléchargez le fichier :download:`ici <ressources/Godot-Cours-Arcadia---Tower-Protector--- Assets.zip>`, extrayez le fichier ``assets`` et mettez-le dans le dossier de votre projet:
.. image:: img/filesAsset.png

Une fois cette étape terminée, nous pouvons commencer à créer notre premier jeu !


heyyy
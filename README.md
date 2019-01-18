
# Pong19 Zero
L'objectif de ce projet est de programmer le jeu d'arcade *Pong* en **Python 3.6.7**
## Auteur
**Yann LE COZ** - Bordeaux Ynov Campus Informatique - [Zocel](https://github.com/Zocel)
## Sommaire
* [Bibliothèques utilisées](#bibliothèques-utilisées)
* [Commandes](#commandes)
* [Menu principal](#menu-principal)
* [Configurations](#configurations)
  * [Arène](#arène)
    * [Taille de l'Arène](#taille-de-larène)
    * [Couleur de l'Arène](#couleur-de-larène)
  * [Nombre de points gagnants](#nombre-de-points-gagnants)
  * [Raquettes](#raquettes)
  * [Balle](#balle)
    * [Vitesse de la Balle](#vitesse-de-la-balle)
    * [Couleur de la Balle](#couleur-de-la-balle)
* [Partie](#partie)
    * [Les Règles du *Pong*](#les-règles-du-pong)
    * [Mettre en pause une partie](#mettre-en-pause-une-partie)
* [Fin de partie](#fin-de-partie)
* [**Licence**](#licence)

## Bibliothèques utilisées
* Tkinter
* Math
* Time

## Commandes
> *Le jeu a été conçu pour être joué à deux joueurs.*

- **Raquette de gauche :**
    * Se déplacer en Haut : `R`
    * Se déplacer en Bas : `F`
- **Raquette de droite :**
    * Se déplacer en Haut : `↑`
    * Se déplacer en Bas : `↓`
- **Mettre en pause la partie :** `Ctrl+P`

## Menu principal
À l'ouverture de l'application `main.py`, l'écran du **menu principal** est le premier à apparaître.
Vous aurez alors explicitement le choix entre **Faire une partie** ou **Quitter** le jeu directement.

## Configurations
### Arène
#### Taille de l'Arène
Grâce à la liste déroulante *Taille de l'Arène* vous pouvez choisir entre **trois** types de taille :
* **Entraînement**
* **Basique**
* **Tournoi**
#### Couleur de l'Arène
À partir de la liste déroulante *Couleur de l'Arène* vous pouvez choisir **deux** thèmes de couleur :
* **Défaut**
* **Négatif**
### Nombre de points gagnants
Le champ de saisie en-dessous de *Nombre de points gagnants*  vous permet d'entrer le nombre de points gagnants de la partie de jeu.

> **Nombre de points gagnants** est égal à la *différence de score* du joueur de gauche et du joueur de droite.
> Le nombre que vous entrerez  dans le champ de saisie doit être également **supérieur à 0**.

### Raquettes
Grâce à la liste déroulante *Couleur des Raquettes* vous avez le choix entre **quatre** couleurs pour vos raquettes :
* **Défaut**
<br>La couleur des raquettes reste inchangée par rapport aux lignes de terrain.
* **Saphir**
* **Émeraude**
* **Rubis**
### Balle
#### Vitesse de la Balle
La liste déroulante *Vitesse de la balle* vous permet de choisir entre **trois** types de vitesse :
* **Lente**
* **Normale**
* **Rapide**
#### Couleur de la Balle
Grâce à la liste déroulante *Couleur de la Balle* vous avez le choix la balle entre les **quatre** couleurs suivantes :
* **Défaut**
<br>Tout comme la couleur des raquettes, la couleur de la balle reste inchangée par rapport aux lignes de terrain.
* **Saphir**
* **Émeraude**
* **Rubis**

Une fois les configurations que vous souhaitez attribuer à la Partie terminées, appuyez sur le bouton **`Configurer la partie`**.
## Partie
### Les Règles du *Pong*
* À l'aide de leur raquette, les joueurs doivent mettre la balle dans le but adversaire ;
* Les raquettes des joueurs ne peuvent bouger que sur un axe vertical défini ;
* Les raquettes sont restreintes également sur ce même axe aux limites des Arènes.

### Mettre en pause une partie
Vous pouvez mettre le jeu en pause en appuyant sur les touches `Ctrl+P`. Ce qui aura pour effet **de bloquer le déplacement des raquettes et de la balle**.

Une fenêtre devra alors s'ouvrir pour vous indiquer que la partie en cours est en pause mais aussi de vous permettre de **reprendre la partie en cours** ou de tout simplement **quitter l'application**.

## Fin de partie
Une fois le nombre de points gagnants atteint, l'écran de jeu se ferme pour laisser place à un dernière écran : l'écran de **fin de partie**.
Il résume la partie qui vient de se dérouler en affichant le **gagnant** et le **perdant** de la partie avec leur **score respectif** ainsi que la **durée** de celle-ci.
> Le temps est affiché au format `HH : MM : SS`.

De plus, grâce aux boutons **`Refaire une partie`** et **`Aller au menu principal`** vous pouvez soit :
* refaire une partie avec **les même configurations** que la précédentes ;
* retourner au menu principal pour :
	* refaire une partie avec **de nouvelles configurations** ;
	* quitter l'application `main.py`.

## Licence
**GNU GENERAL PUBLIC LICENSE**
Version 3 du 29 Juin 2007

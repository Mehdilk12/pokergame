bonjour ,
veuillez utiliser le compilateur  https://codeboot.org/py/ puisque des des images et quelques éléments  sont pré-enregistrer par le professeur la bas merci :D
voici l'énoncé:
1. Introduction
Ce travail pratique consiste à développer une application web pour jouer au jeu poker shuffle. C'est un jeu joué en solitaire (un seul joueur) avec des cartes à jouer standard (52 cartes). Le jeu consiste à piger 25 cartes une à la fois et les placer dans une grille 5 par 5 pour former des mains de poker sur les 5 rangées et 5 colonnes.

Chaque main de poker (une paire, deux paires, full house, etc.) a un nombre de points correspondants. Le joueur doit tenter de maximiser le pointage total, c'est-à-dire la somme des points pour les 5 rangées et 5 colonnes. Lorsque le joueur place la 25ième carte, le jeu se termine et le programme affiche le pointage final puis redémarre une nouvelle partie. Avant la fin de la partie le joueur peut déplacer les cartes sur la grille. Il peut aussi recommencer une nouvelle partie en cliquant sur un bouton.

Un modèle complètement fonctionnel du jeu est disponible à l'adresse suivante: http://www.iro.umontreal.ca/~feeley/tp2.html. Votre travail consiste donc à imiter son comportement le plus fidèlement possible à l'intérieur de l'environnement codeBoot.

2. Mains de poker et pointage
Une main de poker est un groupe de 5 cartes. Voici les différentes mains de poker et le pointage associé, par ordre décroissant de pointage :

(100 points) Quinte Flush Royale : L'as, le roi, la dame, le valet et le 10 d'une même couleur (tous trèfle, tous pique, tous carreau, ou tous coeur).
(75 points) Quinte Flush : Cinq cartes de même couleur qui se suivent (par exemple le 7, 8, 9, 10 et le valet, tous trèfle, tous pique, tous carreau, ou tous coeur).
(50 points) Carré : Quatre cartes de même valeur (par exemple quatre valets).
(25 points) Full House : Trois cartes de même valeur et une paire de cartes de même valeur (par exemple trois as et deux 9).
(20 points) Couleur ou Flush : Toutes les cartes de même couleur (tous trèfle, tous pique, tous carreau, ou tous coeur).
(15 points) Quinte : Cinq cartes qui se suivent (par exemple le 8, 9, 10, valet et dame). Il est à noter que l'as peut être le début ou la fin de la séquence.
(10 points) Brelan : Trois cartes de même valeur (par exemple trois rois).
(5 points) Double Paire : Une paire de cartes de même valeur et une autre paire de cartes de même valeur (par exemple deux rois et deux 7).
(2 points) Une Paire : Une paire de cartes de même valeur (par exemple deux as).

# pygame-chess

Implémentation avec pygame des règles (complètes) d'un jeu d'échecs

Il requiert une version de Python 3.9+ ainsi que la librairie pygame.

Les versions ./vX/ sont des versions incrémentales du jeu.

La version finale est dans le répertoire ./v5/ ou bien dans le répertoire ./refactoring-v1/.

Le jeu se lance ainsi :

```
$ python jeu.py
```

Par défaut, le temps de jeu est de 5 minutes par joueur (TEMPS_PAR_JOUEUR dans le fichier jeu.py) et les pions qui peuvent être pris "en passant" sont affichés sous forme d'un "mini-pion" (méthode deplace dans regles.py). Quand le joueur sélectionne une pièce, les cases possibles sont aussi marquées d'un point de couleur (méthode montreTousLesMouvements dans regles.py). 


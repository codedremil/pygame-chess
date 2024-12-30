import pygame
from pygame import mixer
from echiquier import Echiquier
from ihm import TAILLE_PLATEAU
from ihm import initialise_jeu, affiche_jeu

TEMPS_PAR_JOUEUR = 1

pygame.init()
pygame.font.init()
#mixer.init()

def main():
    fenetre = initialise_jeu()
    clock = pygame.time.Clock()
    plateau = Echiquier(TAILLE_PLATEAU, TEMPS_PAR_JOUEUR)
    counter = 0
    run = True
    while run:
        affiche_jeu(fenetre, plateau)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


if __name__ == "__main__":
    while True:
        main()

# EOF
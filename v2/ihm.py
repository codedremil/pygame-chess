import pygame
from piece import BLANC, NOIR

LARGEUR, HAUTEUR = (1000, 600)
TAILLE_CASE = 70
TAILLE_PLATEAU = 8 * TAILLE_CASE
COULEUR_FOND = (35, 35, 35)
COULEUR_BORD = (100, 149, 237)


def initialise_jeu():
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Jeu d'échec")
    return fenetre


def affiche_jeu(fenetre, plateau):
    fenetre.fill(COULEUR_FOND)
    pygame.draw.rect(fenetre, COULEUR_BORD, (0, 0, HAUTEUR, HAUTEUR))   # carré de l'échiquier
    plateau.dessine(fenetre)
    pygame.display.update()



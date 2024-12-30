from abc import abstractmethod
import logging
import pygame
import os

BLANC = 'blanc'
NOIR = 'noir'

# Encodage des pièces (type_piece)
PION_BLANC = 'P'
PION_NOIR = 'p'
FOU_BLANC = 'F'
FOU_NOIR = 'f'
CAVALIER_BLANC = 'C'
CAVALIER_NOIR ='c'
TOUR_BLANC = 'T'
TOUR_NOIR = 't'
REINE_BLANC = 'Q'
REINE_NOIR = 'q'
ROI_BLANC = 'R'
ROI_NOIR = 'r'

class Piece:
    def __init__(self, ligne, colonne, type_piece, taille):
        logging.debug(f"piece_info: {type_piece}")
        self.ligne, self.colonne, self.taille = ligne, colonne, taille
        self.couleur = BLANC if type_piece <= 'Z' else NOIR
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("ressources", ('B-' if self.couleur == BLANC else 'N-') + type_piece + ".svg")), (250, 250) # (taille * 4, taille * 4)
        )

        self.a_bouge = False    # pour gérer le roque
        self.deplacements = []

    @abstractmethod
    def chercheTousLesDeplacements(self, plateau):
        pass


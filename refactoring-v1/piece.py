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
        curdir = os.path.dirname(__file__)
        file_type = ".png"  # ou ".svg"
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join(curdir, "ressources", ('B-' if self.couleur == BLANC else 'N-') + type_piece + file_type)), (taille, taille)
        )
        self.image.set_colorkey((255, 255, 255))   # pour les PNG
        self.a_bouge = False    # pour gérer le roque
        self.deplacements = []

    @abstractmethod
    def chercheTousLesDeplacements(self, plateau):
        pass

    def deplacementPossible(self, ligne, colonne, plateau, deplacements):
        if 0 <= ligne < 8 and 0 <= colonne < 8:
            piece = plateau.obtientPiece(ligne, colonne)
            if piece is None :
                deplacements.append((ligne, colonne))
                return True

            if piece.couleur != self.couleur:
                deplacements.append((ligne, colonne))
                return False

        return False


    def deplacementDiagonal(self, plateau):
        deplacements = []
        i, j, mouvt = self.ligne - 1, self.colonne - 1, True
        while i >= 0 and j >= 0 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            i -= 1
            j -= 1

        i, j, mouvt = self.ligne + 1, self.colonne - 1, True
        while i < 8 and j >= 0 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            i += 1
            j -= 1

        i, j, mouvt = self.ligne + 1, self.colonne + 1, True
        while i < 8 and j < 8 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            i += 1
            j += 1

        i, j, mouvt = self.ligne - 1, self.colonne + 1, True
        while i >= 0 and j < 8 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            i -= 1
            j += 1

        return deplacements

    def deplacementLateral(self, plateau):
        deplacements = []
        i, j, mouvt = self.ligne - 1, self.colonne, True
        while i >= 0 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            i -= 1

        i, j, mouvt = self.ligne + 1, self.colonne, True
        while i < 8 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            i += 1

        i, j, mouvt = self.ligne, self.colonne - 1, True
        while j >= 0 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            j -= 1

        i, j, mouvt = self.ligne, self.colonne + 1, True
        while j < 8 and mouvt:
            mouvt = self.deplacementPossible(i, j, plateau, deplacements)
            j += 1

        return deplacements

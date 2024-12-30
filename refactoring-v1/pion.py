import pygame
from piece import Piece, BLANC, NOIR
from piece import TOUR_BLANC, TOUR_NOIR, FOU_BLANC, FOU_NOIR, CAVALIER_BLANC, CAVALIER_NOIR, REINE_BLANC, REINE_NOIR
from reine import Reine
from cavalier import Cavalier
from fou import Fou
from tour import Tour


class Pion(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []
        # variables locales pour simplifier l'algorithme
        ligne = self.ligne
        colonne = self.colonne

        if self.couleur == BLANC:
            if ligne - 1 >= 0 and (plateau.obtientPiece(ligne - 1, colonne) is None):
                deplacements.append((ligne - 1, colonne))

            # si le pion est sur sa ligne de départ, il peut peut-être se déplacer de 2 cases ?
            if ligne == 6:
                if (plateau.obtientPiece(5, colonne) is None) and (plateau.obtientPiece(4, colonne) is None):
                    deplacements.append((ligne - 2, colonne))

            # prise en diagonale ?
            if ligne - 1 >= 0:
                if colonne + 1 < 8:
                    piece = plateau.obtientPiece(ligne - 1, colonne + 1)
                    if piece is not None and piece.couleur == NOIR:
                        deplacements.append((ligne - 1, colonne + 1))
                if colonne - 1 >= 0:
                    piece = plateau.obtientPiece(ligne - 1, colonne - 1)
                    if piece is not None and piece.couleur == NOIR:
                        deplacements.append((ligne - 1, colonne - 1))
        else: # NOIR
            if ligne + 1 < 8 and (plateau.obtientPiece(ligne + 1, colonne) is None):
                deplacements.append((ligne + 1, colonne))

            # si le pion est  sur sa ligne de départ, déplacement de 2 cases ?
            if ligne == 1:
                if (plateau.obtientPiece(2, colonne) is None) and (plateau.obtientPiece(3, colonne) is None):
                    deplacements.append((ligne + 2, colonne))

            # prise en diagonale ?
            if ligne + 1 < 8:
                if colonne + 1 < 8:
                    piece = plateau.obtientPiece(ligne + 1, colonne + 1)
                    if piece is not None and piece.couleur == BLANC:
                        deplacements.append((ligne + 1, colonne + 1))
                if colonne - 1 >= 0:
                    piece = plateau.obtientPiece(ligne + 1, colonne - 1)
                    if piece is not None and piece.couleur == BLANC:
                        deplacements.append((ligne + 1, colonne - 1))

        return deplacements

    def promotion(self, plateau):
        run = True
        couleur = self.couleur[0].upper()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if chr(event.key) == "r":
                        plateau[self.ligne][self.colonne].piece = Reine(
                            self.ligne, self.colonne, REINE_NOIR if self.couleur == NOIR else REINE_BLANC, self.taille
                        )
                        return
                    elif chr(event.key) == "c":
                        plateau[self.ligne][self.colonne].piece = Cavalier(
                            self.ligne, self.colonne, CAVALIER_NOIR if self.couleur == NOIR else CAVALIER_BLANC, self.taille
                        )
                        return
                    elif chr(event.key) == "f":
                        plateau[self.ligne][self.colonne].piece = Fou(
                            self.ligne, self.colonne, FOU_NOIR if self.couleur == NOIR else FOU_BLANC, self.taille
                        )
                        return
                    elif chr(event.key) == "t":
                        plateau[self.ligne][self.colonne].piece = Tour(
                            self.ligne, self.colonne, TOUR_NOIR if self.couleur == NOIR else TOUR_BLANC, self.taille
                        )
                        return


# Pion utilisé pour permettre la "prise en passant"
class PionFantome(Piece):
    def chercheTousLesDeplacements(self, plateau):
        return []
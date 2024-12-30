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
        if self.couleur == BLANC:
            if self.ligne == 6:
                if (plateau[5][self.colonne].piece is not None) or (
                        plateau[4][self.colonne].piece is not None
                ):
                    pass
                else:
                    deplacements.append((self.ligne - 2, self.colonne))

            if self.ligne - 1 >= 0 and (plateau[self.ligne - 1][self.colonne].piece is None):
                deplacements.append((self.ligne - 1, self.colonne))

            if self.ligne - 1 >= 0:  # diagonal attack
                if self.colonne + 1 < 8:
                    if (
                            plateau[self.ligne - 1][self.colonne + 1].piece is not None
                            and plateau[self.ligne - 1][self.colonne + 1].piece.couleur == NOIR
                    ):
                        deplacements.append((self.ligne - 1, self.colonne + 1))

                if self.colonne - 1 >= 0:
                    if (
                            plateau[self.ligne - 1][self.colonne - 1].piece is not None
                            and plateau[self.ligne - 1][self.colonne - 1].piece.couleur == NOIR
                    ):
                        deplacements.append((self.ligne - 1, self.colonne - 1))
        else:
            if self.ligne == 1:
                if (plateau[2][self.colonne].piece is not None) or (
                        plateau[3][self.colonne].piece is not None
                ):
                    pass
                else:
                    deplacements.append((self.ligne + 2, self.colonne))

            if self.ligne + 1 < 8 and (plateau[self.ligne + 1][self.colonne].piece is None):
                deplacements.append((self.ligne + 1, self.colonne))

            if self.ligne + 1 < 8:  # diagonal attack
                if self.colonne + 1 < 8:
                    if (
                            plateau[self.ligne + 1][self.colonne + 1].piece is not None
                            and plateau[self.ligne + 1][self.colonne + 1].piece.couleur == BLANC
                    ):
                        deplacements.append((self.ligne + 1, self.colonne + 1))

                if self.colonne - 1 >= 0:
                    if (
                            plateau[self.ligne + 1][self.colonne - 1].piece is not None
                            and plateau[self.ligne + 1][self.colonne - 1].piece.couleur == BLANC
                    ):
                        deplacements.append((self.ligne + 1, self.colonne - 1))

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
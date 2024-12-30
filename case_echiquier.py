import pygame
from roi import Roi
from reine import Reine
from fou import Fou
from cavalier import Cavalier
from tour import Tour
from pion import Pion
from piece import BLANC, NOIR

FOND_BLANC = (240, 240, 255)
FOND_NOIR = (135, 206, 235)

class CaseEchiquier:
    def __init__(self, taille, position, piece_contenue):
        '''
        la valeur de position est un tuple (ligne, colonne)
        la valeur de piece_contenue est chaine comme "ta8"
        '''
        self.taille = taille
        self.ligne = position[0]
        self.colonne = position[1]
        if not len(piece_contenue):
            self.piece = None
        else:
            self.piece = self._associePiece(piece_contenue)

        self._associeCouleur()
        self.est_selectionnee = False

    def _associeCouleur(self):
        # les n°s de ligne et colonne sont tous les 2 pairs ou impairs
        if self.ligne % 2 == self.colonne % 2:
            self.couleur = FOND_BLANC
        else:
            self.couleur = FOND_NOIR

    def _associePiece(self, piece_contenue):
        pieces = {
            'r': Roi,
            'q': Reine,
            't': Tour,
            'c': Cavalier,
            'f': Fou,
            'p': Pion,
        }
        type_piece = piece_contenue[0].lower()
        if type_piece not in pieces:
            raise ValueError(f"Type de pièce inconnu: '{type_piece}' !")

        piece = pieces[type_piece](self.ligne, self.colonne, piece_contenue[0], self.taille)
        return piece

    def dessine(self, fenetre):
        if self.est_selectionnee:
            if self.piece.couleur == BLANC:
                couleur = (65, 105, 225)
            else:
                couleur = (222, 49, 99)
            pygame.draw.rect(
                fenetre,
                couleur,
                (
                    self.colonne * self.taille + 17,
                    self.ligne * self.taille + 17,
                    self.taille + 6,
                    self.taille + 6,
                ),
            )

        pygame.draw.rect(
            fenetre,
            self.couleur,
            (
                self.colonne * self.taille + 20,
                self.ligne * self.taille + 20,
                self.taille,
                self.taille,
            ),
        )
        if self.piece is not None:
            fenetre.blit(self.piece.image, (self.piece.colonne * self.taille + 20,
                                            self.piece.ligne * self.taille + 18))

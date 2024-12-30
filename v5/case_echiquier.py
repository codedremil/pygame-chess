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
CADRE_BLEU = (65, 105, 225)
CADRE_ROUGE = (222, 49, 99)

class CaseEchiquier:
    def __init__(self, taille, index, piece_contenue):
        '''
        la valeur de index est un tuple (ligne, colonne)
        la valeur de piece_contenue est chaine comme "ta8"
        '''
        self.taille = taille
        self.ligne = index[0]
        self.colonne = index[1]
        if not len(piece_contenue):
            self.piece = None
        else:
            self.piece = self._associePiece(piece_contenue)

        self._associeCouleur()
        self.est_selectionnee = False

    def _associeCouleur(self):
        #if (self.ligne % 2 == 0 and self.colonne % 2 == 0) or (self.ligne % 2 != 0 and self.colonne % 2 != 0):
        if self.ligne % 2 == self.colonne % 2:
            self.couleur = FOND_BLANC
        else:
            self.couleur = FOND_NOIR

    def _associePiece(self, piece_contenue):
        type_piece = piece_contenue[0].lower()
        if type_piece == "r":
            return Roi(self.ligne, self.colonne, piece_contenue[0], self.taille)
        elif type_piece == "q":
            return Reine(self.ligne, self.colonne, piece_contenue[0], self.taille)
        elif type_piece == "f":
            return Fou(self.ligne, self.colonne, piece_contenue[0], self.taille)
        elif type_piece == "c":
            return Cavalier(self.ligne, self.colonne, piece_contenue[0], self.taille)
        elif type_piece == "t":
            return Tour(self.ligne, self.colonne, piece_contenue[0], self.taille)
        elif type_piece == "p":
            return Pion(self.ligne, self.colonne, piece_contenue[0], self.taille)
        else:
            raise ValueError(f"Type de pièce inconnu: '{type_piece}' !")

    def dessine(self, fenetre):
        # part5/1: ajout d'un cadre autour de la case sélectionnée
        # la couleur est bleue (BLANC) ou rouge (NOIR)
        if self.est_selectionnee:
            if self.piece.couleur == BLANC:
                couleur = CADRE_BLEU
            else:
                couleur = CADRE_ROUGE
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
            #self.piece.render(fenetre)
            fenetre.blit(self.piece.image, (self.piece.colonne * self.taille + 20, self.piece.ligne * self.taille + 18))

if __name__ == '__main__':
    case1 = CaseEchiquier(10, (3, 4), "")
    assert case1.piece is None

    case2 = CaseEchiquier(10, (3, 5), "r")
    assert type(case2.piece) == Roi

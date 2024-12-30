import logging
from piece import Piece


class Fou(Piece):
    def chercheTousLesDeplacements(self, plateau):
        return self.deplacementDiagonal(plateau)


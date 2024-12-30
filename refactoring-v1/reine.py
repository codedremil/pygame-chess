from piece import Piece


class Reine(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = self.deplacementDiagonal(plateau)
        deplacements.extend(self.deplacementLateral(plateau))
        return deplacements

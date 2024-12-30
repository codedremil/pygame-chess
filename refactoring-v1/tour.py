from piece import Piece


class Tour(Piece):
    def chercheTousLesDeplacements(self, plateau):
        return self.deplacementLateral(plateau)

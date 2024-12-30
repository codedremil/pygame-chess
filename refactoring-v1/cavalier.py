from piece import Piece


class Cavalier(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []

        self.deplacementPossible(self.ligne - 1, self.colonne - 2, plateau, deplacements)
        self.deplacementPossible(self.ligne - 1, self.colonne + 2, plateau, deplacements)
        self.deplacementPossible(self.ligne - 2, self.colonne - 1, plateau, deplacements)
        self.deplacementPossible(self.ligne - 2, self.colonne + 1, plateau, deplacements)
        self.deplacementPossible(self.ligne + 1, self.colonne - 2, plateau, deplacements)
        self.deplacementPossible(self.ligne + 1, self.colonne + 2, plateau, deplacements)
        self.deplacementPossible(self.ligne + 2, self.colonne - 1, plateau, deplacements)
        self.deplacementPossible(self.ligne + 2, self.colonne + 1, plateau, deplacements)

        return deplacements

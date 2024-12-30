from piece import Piece, NOIR, BLANC

class Pion(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []

        # TODO: implémenter la recherche des déplacements !
        # pour l'instant, on fait simple, pas de déplacement initial de 2 cases, pas de prise en diagonale
        if self.couleur == BLANC:
            if self.ligne - 1 >= 0 and (plateau[self.ligne - 1][self.colonne].piece is None):
                deplacements.append((self.ligne - 1, self.colonne))
        else:
            if self.ligne + 1 < 8 and (plateau[self.ligne + 1][self.colonne].piece is None):
                deplacements.append((self.ligne + 1, self.colonne))

        return deplacements

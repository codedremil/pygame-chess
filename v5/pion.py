from piece import Piece, NOIR, BLANC

class Pion(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []

        # variables locales pour simplifier l'algorithme
        ligne = self.ligne
        colonne = self.colonne

        if self.couleur == BLANC:
            if ligne - 1 >= 0 and (plateau[ligne - 1][colonne].piece is None):
                deplacements.append((ligne - 1, colonne))

            # si le pion est sur sa ligne de départ, il peut peut-être se déplacer de 2 cases ?
            if ligne == 6:
                if (plateau[5][colonne].piece is None) and (plateau[4][colonne].piece is None):
                    deplacements.append((ligne - 2, colonne))

            # prise en diagonale ?
            if ligne - 1 >= 0:
                if colonne + 1 < 8:
                    if (
                            plateau[ligne - 1][colonne + 1].piece is not None
                            and plateau[ligne - 1][colonne + 1].piece.couleur == NOIR
                    ):
                        deplacements.append((ligne - 1, colonne + 1))

                if colonne - 1 >= 0:
                    if (
                            plateau[ligne - 1][colonne - 1].piece is not None
                            and plateau[ligne - 1][colonne - 1].piece.couleur == NOIR
                    ):
                        deplacements.append((ligne - 1, colonne - 1))
        else: # NOIR
            if ligne + 1 < 8 and (plateau[ligne + 1][colonne].piece is None):
                deplacements.append((ligne + 1, colonne))

            # si le pion est  sur sa ligne de départ, déplacement de 2 cases ?
            if ligne == 1:
                if (plateau[2][colonne].piece is None) and (plateau[3][colonne].piece is None):
                    deplacements.append((ligne + 2, colonne))

        return deplacements

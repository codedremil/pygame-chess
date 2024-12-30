from piece import Piece


class Cavalier(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []
        if self.ligne - 1 >= 0:
            if self.colonne - 2 >= 0 and (
                    plateau[self.ligne - 1][self.colonne - 2].piece is None
                    or plateau[self.ligne - 1][self.colonne - 2].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne - 1, self.colonne - 2))

            if self.colonne + 2 < 8 and (
                    plateau[self.ligne - 1][self.colonne + 2].piece is None
                    or plateau[self.ligne - 1][self.colonne + 2].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne - 1, self.colonne + 2))

        if self.ligne - 2 >= 0:
            if self.colonne - 1 >= 0 and (
                    plateau[self.ligne - 2][self.colonne - 1].piece is None
                    or plateau[self.ligne - 2][self.colonne - 1].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne - 2, self.colonne - 1))

            if self.colonne + 1 < 8 and (
                    plateau[self.ligne - 2][self.colonne + 1].piece is None
                    or plateau[self.ligne - 2][self.colonne + 1].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne - 2, self.colonne + 1))

        if self.ligne + 1 < 8:
            if self.colonne - 2 >= 0 and (
                    plateau[self.ligne + 1][self.colonne - 2].piece is None
                    or plateau[self.ligne + 1][self.colonne - 2].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne + 1, self.colonne - 2))

            if self.colonne + 2 < 8 and (
                    plateau[self.ligne + 1][self.colonne + 2].piece is None
                    or plateau[self.ligne + 1][self.colonne + 2].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne + 1, self.colonne + 2))

        if self.ligne + 2 < 8:
            if self.colonne - 1 >= 0 and (
                    plateau[self.ligne + 2][self.colonne - 1].piece is None
                    or plateau[self.ligne + 2][self.colonne - 1].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne + 2, self.colonne - 1))

            if self.colonne + 1 < 8 and (
                    plateau[self.ligne + 2][self.colonne + 1].piece is None
                    or plateau[self.ligne + 2][self.colonne + 1].piece.couleur != self.couleur
            ):
                deplacements.append((self.ligne + 2, self.colonne + 1))

        return deplacements

import logging
from piece import Piece


class Fou(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []
        i, j = self.ligne - 1, self.colonne - 1
        while i >= 0 and j >= 0:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break

            deplacements.append((i, j))
            i -= 1
            j -= 1

        i, j = self.ligne + 1, self.colonne - 1
        while i < 8 and j >= 0:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break

            deplacements.append((i, j))
            i += 1
            j -= 1

        i, j = self.ligne + 1, self.colonne + 1
        while i < 8 and j < 8:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break

            deplacements.append((i, j))
            i += 1
            j += 1

        i, j = self.ligne - 1, self.colonne + 1
        while i >= 0 and j < 8:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break
            deplacements.append((i, j))
            i -= 1
            j += 1

        return deplacements


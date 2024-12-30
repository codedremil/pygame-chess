from piece import Piece


class Tour(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []
        i, j = self.ligne - 1, self.colonne
        while i >= 0:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break

            deplacements.append((i, j))
            i -= 1

        i, j = self.ligne + 1, self.colonne
        while i < 8:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break

            deplacements.append((i, j))
            i += 1

        i, j = self.ligne, self.colonne - 1
        while j >= 0:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break

            deplacements.append((i, j))
            j -= 1

        i, j = self.ligne, self.colonne + 1
        while j < 8:
            if plateau[i][j].piece is not None:
                if self.couleur != plateau[i][j].piece.couleur:
                    deplacements.append((i, j))
                break

            deplacements.append((i, j))
            j += 1

        return deplacements

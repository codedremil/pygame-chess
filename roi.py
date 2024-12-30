from piece import Piece
from tour import Tour


class Roi(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []
        if self.ligne - 1 >= 0:
            deplacements.append((self.ligne - 1, self.colonne))
            if self.colonne - 1 >= 0:
                deplacements.append((self.ligne - 1, self.colonne - 1))
            if self.colonne + 1 < 8:
                deplacements.append((self.ligne - 1, self.colonne + 1))

        if self.ligne + 1 < 8:
            deplacements.append((self.ligne + 1, self.colonne))
            if self.colonne - 1 >= 0:
                deplacements.append((self.ligne + 1, self.colonne - 1))
            if self.colonne + 1 < 8:
                deplacements.append((self.ligne + 1, self.colonne + 1))

        if self.colonne - 1 >= 0:
            deplacements.append((self.ligne, self.colonne - 1))
            # if self.ligne - 1 >= 0:
            #     deplacements.append((self.ligne - 1, self.colonne - 1))
            # if self.ligne + 1 < 8:
            #     deplacements.append((self.ligne + 1, self.ligne - 1))

        if self.colonne + 1 < 8:
            deplacements.append((self.ligne, self.colonne + 1))
            # if self.ligne - 1 >= 0:
            #     deplacements.append((self.ligne - 1, self.colonne + 1))
            # if self.ligne + 1 < 8:
            #     deplacements.append((self.ligne + 1, self.colonne + 1))

        # Il faut supprimer les mouvements qui risquent une mise en échec
        deplacements_finaux = []
        for deplacement in deplacements:
            """
            Weird bug with king moves. It appends some extra moves to list
            Haven't found the bug yet but the the next two lines fix that
            """
            # if abs(deplacement[0] - self.ligne) > 1 or abs(deplacement[1] - self.colonne) > 1:
            #     continue
            piece = plateau[deplacement[0]][deplacement[1]].piece
            """
            Append to final_moves if it's a valid move
            """
            if piece is None or piece.couleur != self.couleur:
                deplacements_finaux.append(deplacement)

        # Ajout des possibilités de roque
        if not self.a_bouge:
            case_petit_roque = plateau[self.ligne][7]
            case_grand_roque = plateau[self.ligne][0]
            if (
                    type(case_petit_roque.piece) == Tour and
                    case_petit_roque.piece.couleur == self.couleur and
                    not case_petit_roque.piece.a_bouge and
                    plateau[self.ligne][5].piece is None and
                    plateau[self.ligne][6].piece is None
            ):
                deplacements_finaux.append((self.ligne, self.colonne + 2))

            if (
                    type(case_grand_roque.piece) == Tour and
                    case_grand_roque.piece.couleur == self.couleur and
                    not case_grand_roque.piece.a_bouge and
                    plateau[self.ligne][1].piece is None and
                    plateau[self.ligne][2].piece is None and
                    plateau[self.ligne][3].piece is None
            ):
                deplacements_finaux.append((self.ligne, self.colonne - 2))

        return deplacements_finaux

from piece import Piece
from tour import Tour


class Roi(Piece):
    def chercheTousLesDeplacements(self, plateau):
        deplacements = []

        self.deplacementPossible(self.ligne - 1, self.colonne - 1, plateau, deplacements)
        self.deplacementPossible(self.ligne - 1, self.colonne, plateau, deplacements)
        self.deplacementPossible(self.ligne - 1, self.colonne + 1, plateau, deplacements)
        self.deplacementPossible(self.ligne, self.colonne - 1, plateau, deplacements)
        self.deplacementPossible(self.ligne, self.colonne + 1, plateau, deplacements)
        self.deplacementPossible(self.ligne + 1, self.colonne - 1, plateau, deplacements)
        self.deplacementPossible(self.ligne + 1, self.colonne, plateau, deplacements)
        self.deplacementPossible(self.ligne + 1, self.colonne + 1, plateau, deplacements)

        # Il faut supprimer les mouvements qui risquent une mise en échec:
        # NON, ceci est systématiquement fait dans la fonction "montreTousLesMouvements" de regles.py
        # deplacements_finaux = []
        # for deplacement in deplacements:
        #     piece = plateau.obtientPiece(deplacement[0], deplacement[1])
        #     if piece is None or piece.couleur != self.couleur:
        #         deplacements_finaux.append(deplacement)

        # Ajout des possibilités de roque
        if not self.a_bouge:
            case_petit_roque = plateau.obtientPiece(self.ligne, 7)
            case_grand_roque = plateau.obtientPiece(self.ligne, 0)
            if (
                    type(case_petit_roque) == Tour and
                    case_petit_roque.couleur == self.couleur and
                    not case_petit_roque.a_bouge and
                    plateau.obtientPiece(self.ligne, 5) is None and
                    plateau.obtientPiece(self.ligne, 6) is None
            ):
                deplacements.append((self.ligne, self.colonne + 2))

            if (
                    type(case_grand_roque) == Tour and
                    case_grand_roque.couleur == self.couleur and
                    not case_grand_roque.a_bouge and
                    plateau.obtientPiece(self.ligne, 1) is None and
                    plateau.obtientPiece(self.ligne, 2) is None and
                    plateau.obtientPiece(self.ligne, 3) is None
            ):
                deplacements.append((self.ligne, self.colonne - 2))

        return deplacements

import pygame
from case_echiquier import CaseEchiquier

NB_COLS = 8
NB_LIGNES = 8
COULEUR_BLANC = (255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont("Sans Serif", 30)

class Echiquier:
    positions_initiales = [
        "ta8", "cb8", "fc8", "qd8", "re8", "ff8", "cg8", "th8",
        "pa7", "pb7", "pc7", "pd7", "pe7", "pf7", "pg7", "ph7",
        "Pa2", "Pb2", "Pc2", "Pd2", "Pe2", "Pf2", "Pg2", "Ph2",
        "Ta1", "Cb1", "Fc1", "Qd1", "Re1", "Ff1", "Cg1", "Th1",
    ]

    HORIZONTAL_MAPPING = list('abcdefgh')
    VERTICAL_MAPPING = [i for i in range(NB_LIGNES, 0, -1)]

    def __init__(self, largeur, temps_par_joueur):  # temps_par_joueur inutile
        self.largeur = largeur
        self.taille_case = self.largeur // NB_COLS

        # On remplit avec que du vide !
        self.cases_echiquier = [[CaseEchiquier(self.taille_case, (i, j), "") for j in range(NB_COLS)]
                                for i in range(NB_LIGNES)]

        for piece in self.positions_initiales:
            ligne = NB_LIGNES - (int(piece[2]) - 1) - 1
            col = ord(piece[1]) - ord('a')
            self.cases_echiquier[ligne][col] = CaseEchiquier(self.taille_case, (ligne, col), piece)

    def dessine(self, fenetre):
        # Ecrit le nom des lignes et des colonnes
        for i, h in enumerate(self.HORIZONTAL_MAPPING):
            text = font.render(h, False, COULEUR_BLANC)
            fenetre.blit(text, (i * self.taille_case + 50, 0))
            fenetre.blit(text, (i * self.taille_case + 50, 580))

        for j, v in enumerate(self.VERTICAL_MAPPING):
            text = font.render(str(v), False, COULEUR_BLANC)
            fenetre.blit(text, (5, j * self.taille_case + 45))
            fenetre.blit(text, (585, j * self.taille_case + 45))

        # Dessine les cases
        for ligne in self.cases_echiquier:
            for case_echiquier in ligne:
                case_echiquier.dessine(fenetre)


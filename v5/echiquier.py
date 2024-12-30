import pygame
from case_echiquier import CaseEchiquier
from regles import Regles
from joueur import Joueur   # v3
from piece import BLANC, NOIR   # v3
from ihm import affiche_message_centre  # v3

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

    def __init__(self, largeur, temps_par_joueur, jeu_initial=None):  # temps_par_joueur inutile
        self.largeur = largeur
        self.taille_case = self.largeur // NB_COLS

        # Ajout v3
        self.noir = Joueur(NOIR, temps_par_joueur)
        self.blanc = Joueur(BLANC, temps_par_joueur)
        self.gagnant = None
        self.raison_victoire = ""
        self.echec_en_cours = None
        self.echec_alerte = False
        self.case_selectionnee = None
        self.partie_nulle = False

        # On remplit avec que du vide !
        self.cases_echiquier = [[CaseEchiquier(self.taille_case, (i, j), "") for j in range(NB_COLS)]
                                for i in range(NB_LIGNES)]

        # part5/4: Soit c'est une nouvelle partie, soit c'est un jeu précis
        pieces_depart = jeu_initial['pieces'] if jeu_initial is not None else self.positions_initiales
        #for piece in self.positions_initiales:
        for piece in pieces_depart:
            ligne = NB_LIGNES - (int(piece[2]) - 1) - 1
            col = ord(piece[1]) - ord('a')
            self.cases_echiquier[ligne][col] = CaseEchiquier(self.taille_case, (ligne, col), piece)

    def dessine(self, fenetre):
        # v3
        if self.blanc.time <= 0:
            self.raison_victoire = "Temps écoulé"
            self.gagnant = NOIR
        if self.noir.time <= 0:
            self.raison_victoire = "Temps écoulé"
            self.gagnant = BLANC

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

        # v4
        # Montre les mouvements de la pièce sélectionnée, si elle existe
        if self.case_selectionnee is not None:
            self.case_selectionnee.dessine(fenetre)
            Regles.montreTousLesMouvements(self.case_selectionnee.piece, self, fenetre)

        # part5/3: prise en compte de la fin de jeu
        if self.gagnant is not None:
            return

        # v3
        self.blanc.afficheTempsRestant(fenetre) # (760, 570))
        self.noir.afficheTempsRestant(fenetre) # (760, 10))

        if self.blanc.a_le_trait:
            affiche_message_centre(fenetre, 50, "Trait aux Blancs")
        else:
            affiche_message_centre(fenetre, 50, "Trait aux Noirs")

    # v4/2
    def determineLaCase(self, position):
        x, y = position[0] - 20, position[1] - 20
        for ligne in self.cases_echiquier:
            for case_echiquier in ligne:
                vert = case_echiquier.ligne * case_echiquier.taille
                horiz = case_echiquier.colonne * case_echiquier.taille
                if vert <= y <= vert + case_echiquier.taille and horiz <= x <= horiz + case_echiquier.taille:
                    return case_echiquier

    # v4/2
    def selectionneLaCase(self, une_case):
        # Si une case est déjà sélectionnée: capture ou déplacement ?

        # v5? ouv4/9 déplace la pièce sélectionnée
        if self.case_selectionnee:
            case_selectionnee = (une_case.ligne, une_case.colonne)
            deplacements = self.case_selectionnee.piece.deplacements
            if case_selectionnee in deplacements:  # déplace ou capture une pièce ?
                Regles.deplace(self.case_selectionnee.piece, self.case_selectionnee, une_case, self)
                self.deselectionneLaCase()
                self.blanc.inverseLeTour()
                self.noir.inverseLeTour()
                return

        # quel est le joueur ?
        joueur = BLANC if self.blanc.a_le_trait else NOIR

        if self.case_selectionnee:
            self.case_selectionnee.est_selectionnee = False
            self.case_selectionnee = None
            if self.case_selectionnee == une_case:
                self.deselectionneLaCase()
                return

            if une_case is not None and une_case.piece is not None and une_case.piece.couleur == joueur:
                une_case.est_selectionnee = True
                self.case_selectionnee = une_case

            return

        if une_case is not None and une_case.piece is not None and une_case.piece.couleur == joueur:
            une_case.est_selectionnee = True
            self.case_selectionnee = une_case

    # v4/2
    def deselectionneLaCase(self):
        if self.case_selectionnee:
            self.case_selectionnee.est_selectionnee = False
            self.case_selectionnee = None

import logging
import pygame
#from pygame import mixer
from case_echiquier import CaseEchiquier
from joueur import Joueur
from piece import BLANC, NOIR
from regles import Regles
from ihm import affiche_message_centre

NB_COLS = 8
NB_LIGNES = 8

pygame.font.init()
#mixer.init()
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

    def __init__(self, largeur, temps_par_joueur, jeu_initial=None):
        self.largeur = largeur
        self.taille_case = self.largeur // NB_COLS
        self.noir = Joueur(NOIR, temps_par_joueur)
        self.blanc = Joueur(BLANC, temps_par_joueur)
        self.gagnant = None
        self.raison_victoire = ""
        self.echec_en_cours = None
        self.echec_alerte = False
        self.case_selectionnee = None
        self.partie_nulle = False

        # On remplit avec que du vide !
        self.cases_echiquier = [[CaseEchiquier(self.taille_case, (i, j), "") for j in range(NB_COLS)] for i in range(NB_LIGNES)]

        # Soit c'est une nouvelle partie, soit c'est un jeu précis
        pieces_depart = jeu_initial['pieces'] if jeu_initial is not None else self.positions_initiales
        for piece in pieces_depart:
            ligne = NB_LIGNES - (int(piece[2]) - 1) - 1
            col = ord(piece[1]) - ord('a')
            self.cases_echiquier[ligne][col] = CaseEchiquier(self.taille_case, (ligne, col), piece)

        logging.debug(self.cases_echiquier)

        if jeu_initial is not None and jeu_initial['tour'] != 'blanc':
            self.blanc.inverseLeTour()
            self.noir.inverseLeTour()

        Regles.debut_partie(self)


    def determineLaCase(self, position):
        x, y = position[0] - 20, position[1] - 20
        for ligne in self.cases_echiquier:
            for case_echiquier in ligne:
                if (
                        case_echiquier.ligne * case_echiquier.taille <= y <= case_echiquier.ligne * case_echiquier.taille + case_echiquier.taille
                        and case_echiquier.colonne * case_echiquier.taille <= x <= case_echiquier.colonne * case_echiquier.taille + case_echiquier.taille
                ):
                    return case_echiquier


    def selectionneLaCase(self, une_case):
        # Si une case est déjà sléectionnée: capture ou déplacement ?
        if self.case_selectionnee:
            case_selectionnee = (une_case.ligne, une_case.colonne)
            deplacements = self.case_selectionnee.piece.deplacements
            if case_selectionnee in deplacements:  # déplace ou capture une pièce ?
                Regles.deplace(self.case_selectionnee.piece, self.case_selectionnee, une_case, self)
                self.deselectionneLaCase()
                self.blanc.inverseLeTour()
                self.noir.inverseLeTour()
                return

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


    def deselectionneLaCase(self):
        if self.case_selectionnee:
            self.case_selectionnee.est_selectionnee = False
            self.case_selectionnee = None


    def dessine(self, fenetre):
        if self.blanc.time <= 0:
            self.raison_victoire = "Temps écoulé"
            self.gagnant = NOIR
        if self.noir.time <= 0:
            self.raison_victoire = "Temps écoulé"
            self.gagnant = BLANC

        a_le_trait = BLANC if self.blanc.a_le_trait else NOIR
        mouvements_possibles = []
        for ligne in self.cases_echiquier:
            for case_echiquier in ligne:
                if case_echiquier.piece is not None and case_echiquier.piece.couleur == a_le_trait:
                    logging.debug(f"montreTousLesMouvements {case_echiquier.piece}")
                    deplacements = Regles.montreTousLesMouvements(case_echiquier.piece, self, fenetre)
                    if len(deplacements):
                        mouvements_possibles.extend(deplacements)

        # print(self.__total_moves, turn, all_possible_moves)
        if not len(mouvements_possibles):
            if self.echec_en_cours is None:
                self.gagnant = "PAT"
            else:
                self.gagnant = BLANC if self.noir.a_le_trait else NOIR
                self.raison_victoire = "MAT"

        # Ecrit le nom des lignes et des colonnes
        for i, h in enumerate(self.HORIZONTAL_MAPPING):
            text = font.render(h, False, (255, 255, 255))
            fenetre.blit(text, (i * self.taille_case + 50, 0))
            fenetre.blit(text, (i * self.taille_case + 50, 580))

        for j, v in enumerate(self.VERTICAL_MAPPING):
            text = font.render(str(v), False, (255, 255, 255))
            fenetre.blit(text, (5, j * self.taille_case + 45))
            fenetre.blit(text, (585, j * self.taille_case + 45))

        # Dessine les cases
        for ligne in self.cases_echiquier:
            for case_echiquier in ligne:
                case_echiquier.dessine(fenetre)

        # Montre les mouvements de la pièce sélectionnée, si elle existe
        if self.case_selectionnee is not None:
            self.case_selectionnee.dessine(fenetre)
            Regles.montreTousLesMouvements(self.case_selectionnee.piece, self, fenetre)

        if self.gagnant is not None:
            logging.debug("Jeu terminé")
            return

        self.blanc.afficheTempsRestant(fenetre) # (760, 570))
        self.noir.afficheTempsRestant(fenetre) # (760, 10))

        if self.blanc.a_le_trait:
            affiche_message_centre(fenetre, 50, "Trait aux Blancs")
        else:
            affiche_message_centre(fenetre, 50, "Trait aux Noirs")

        if self.echec_en_cours is not None:
            if self.echec_alerte:
                #pygame.mixer.music.load("Assets/music/Alert02.wav")
                #pygame.mixer.music.play()
                self.echec_alerte = False

            affiche_message_centre(fenetre, 45, "Echec !", (255, 0, 0), 510 if self.echec_en_cours == BLANC else 90)

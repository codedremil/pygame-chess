import pygame
from piece import BLANC, NOIR, PION_BLANC, PION_NOIR
from roi import Roi

# Implémente les règles du jeu d'échec
class Regles:
    @classmethod
    def montreTousLesMouvements(cls, piece, echiquier, fenetre):
        '''
        Montre tous les mouvements possibles d'une pièce sélectionnée.
        TODO: Il faut supprimer les mouvements pouvant aboutir à un échec du roi du joueur
        '''
        plateau = echiquier.cases_echiquier
        piece.deplacements = []

        temp_depls = piece.chercheTousLesDeplacements(plateau)  # il faut calculer les déplacements
        # for deplacement in temp_depls:
        #     case_courante = plateau[piece.ligne][piece.colonne]
        #     nouvelle_case = plateau[deplacement[0]][deplacement[1]]
        #     piece.ligne, piece.colonne = nouvelle_case.ligne, nouvelle_case.colonne
        #     piece_precedente = nouvelle_case.piece  # storing what is currently in the new cell
        #     nouvelle_case.piece = piece
        #     case_courante.piece = None
        #
        #     # cherche l'emplacement du roi
        #     emplacement_du_roi = (0, 0)
        #     tous_les_deplacements_adversaire = []
        #     for ligne in plateau:
        #         for case_echiquier in ligne:
        #             if case_echiquier.piece is not None and case_echiquier.piece.couleur == piece.couleur:
        #                 if type(case_echiquier.piece) == Roi:
        #                     emplacement_du_roi = (
        #                         case_echiquier.piece.ligne,
        #                         case_echiquier.piece.colonne,
        #                     )
        #
        #             if case_echiquier.piece is not None and case_echiquier.piece.couleur != piece.couleur:
        #                 deplacements_adversaire = case_echiquier.piece.chercheTousLesDeplacements(plateau)
        #                 if len(deplacements_adversaire):
        #                     tous_les_deplacements_adversaire.extend(deplacements_adversaire)

            # # revient en arrière
            # piece.ligne, piece.colonne = case_courante.ligne, case_courante.colonne
            # case_courante.piece = piece
            # nouvelle_case.piece = piece_precedente  # restaure la pièce sauvée
            # if emplacement_du_roi not in tous_les_deplacements_adversaire:
            #     piece.deplacements.append(deplacement)

        # A supprimer en v5:
        piece.deplacements = temp_depls

        couleur = (65, 105, 225) if piece.couleur == BLANC else (222, 49, 99)
        for deplacement in piece.deplacements:
            pygame.draw.circle(fenetre, couleur, (deplacement[1] * 70 + 56, deplacement[0] * 70 + 56), 9)

        return piece.deplacements


    @classmethod
    def deplace(cls, piece, case_courante, nouvelle_case, echiquier):
        """
        Déplace la pièce si le déplacement est valide sans mise en échec
        """
        plateau = echiquier.cases_echiquier

        # TODO: nombre de coups sans prise, nombre de positions répétées
        # TODO: Cas du Pion qui fait 2 cases avec ppossibilité de "prise en passant"
        # TODO: Gestion du roque

        piece.ligne, piece.colonne = nouvelle_case.ligne, nouvelle_case.colonne
        if nouvelle_case.piece is not None:
            cls.nb_coups_sans_prise = 0

        nouvelle_case.piece = piece
        case_courante.piece = None

        piece.a_bouge = True

        # TODO: Promotion du pion

        # TODO: Alerte si l'adversaire est en échec

        # TODO: Echec ?

        echiquier.echec_en_cours = None

        # TODO: Implémente les parties nulles:
        # 2 cas: 50 coups sont prises de pièces ou bien 3 fois la même situation

        # movement_sound = (
        #     pygame.mixer.Sound("Assets/music/capture.wav")
        #     if capture
        #     else pygame.mixer.Sound("Assets/music/move.wav")
        # )
        # movement_sound.play()

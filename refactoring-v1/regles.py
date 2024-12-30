import logging
import pygame
from piece import BLANC, NOIR, PION_BLANC, PION_NOIR
from roi import Roi
from pion import Pion, PionFantome
from ihm import affichage_promotion_pion


class Regles:
    pion_fantome_blanc = None
    pion_fantome_noir = None
    historique_positions = []
    nb_coups_sans_prise = 0
    nb_coups = 1

    @classmethod
    def debut_partie(cls, echiquier):
        cls.historique_positions = []
        cls.memorise(echiquier)

    @classmethod
    def montreTousLesMouvements(cls, piece, echiquier, fenetre):
        '''
        Montre tous les mouvements possibles d'une pièce sélectionnée.
        Il faut supprimer les mouvements pouvant aboutir à un échec du roi du joueur
        '''
        plateau = echiquier.cases_echiquier
        piece.deplacements = []

        #temp_depls = piece.chercheTousLesDeplacements(plateau)
        temp_depls = piece.chercheTousLesDeplacements(echiquier)
        ''' 
        Pour chaque déplacement, on le simule et on calcule tous les déplacements
        de l'adversaire. Si un déplacement de l'adversaire permettrait d'atteindre le roi du joueur,
        le déplacement est interdit (pièce clouée ou roi interdit de déplacement)
        '''
        for deplacement in temp_depls:
            case_courante = plateau[piece.ligne][piece.colonne]
            nouvelle_case = plateau[deplacement[0]][deplacement[1]]
            piece.ligne, piece.colonne = nouvelle_case.ligne, nouvelle_case.colonne
            piece_precedente = nouvelle_case.piece  # storing what is currently in the new cell
            nouvelle_case.piece = piece
            case_courante.piece = None

            # cherche l'emplacement du roi
            emplacement_du_roi = (0, 0)
            tous_les_deplacements_adversaire = []
            for ligne in plateau:
                for case_echiquier in ligne:
                    if case_echiquier.piece is not None and case_echiquier.piece.couleur == piece.couleur:
                        if type(case_echiquier.piece) == Roi:
                            emplacement_du_roi = (
                                case_echiquier.piece.ligne,
                                case_echiquier.piece.colonne,
                            )
                            logging.debug("[Alerte]: Roi trouvé")
                            logging.debug(f"[Position du Roi]: {emplacement_du_roi}")

                    if case_echiquier.piece is not None and case_echiquier.piece.couleur != piece.couleur:
                        #deplacements_adversaire = case_echiquier.piece.chercheTousLesDeplacements(plateau)
                        deplacements_adversaire = case_echiquier.piece.chercheTousLesDeplacements(echiquier)
                        if len(deplacements_adversaire):
                            tous_les_deplacements_adversaire.extend(deplacements_adversaire)

            # revient en arrière
            piece.ligne, piece.colonne = case_courante.ligne, case_courante.colonne
            case_courante.piece = piece
            nouvelle_case.piece = piece_precedente  # restaure la pièce sauvée
            if emplacement_du_roi not in tous_les_deplacements_adversaire:
                piece.deplacements.append(deplacement)

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
        cls.nb_coups_sans_prise += 1
        if piece.couleur == NOIR:
            cls.nb_coups += 1

        # Si pion se déplace de 2 cases au début, il faut créer un PionFantome pour permettre la "prise en passant"
        if type(piece) == Pion and piece.a_bouge == False:
            if piece.couleur == BLANC and nouvelle_case.ligne == 4:
                cls.pion_fantome_blanc = PionFantome(5, nouvelle_case.colonne, PION_BLANC, piece.taille // 2)
                plateau[5][nouvelle_case.colonne].piece = cls.pion_fantome_blanc

            if piece.couleur == NOIR and nouvelle_case.ligne == 3:
                cls.pion_fantome_noir = PionFantome(2, nouvelle_case.colonne, PION_NOIR, piece.taille // 2)
                plateau[2][nouvelle_case.colonne].piece = cls.pion_fantome_noir

        # Si le pion "prend en passant" l'adversaire, il faut supprimer le véritable Pion
        if type(nouvelle_case.piece) == PionFantome:
            cls.nb_coups_sans_prise = 0
            if nouvelle_case.piece.couleur == BLANC:
                plateau[4][nouvelle_case.colonne].piece = None
            else:
                plateau[3][nouvelle_case.colonne].piece = None

        # Si l'adversaire a un pion fantôme, il faut le supprimer
        if case_courante.piece.couleur == NOIR and cls.pion_fantome_blanc is not None:
            plateau[cls.pion_fantome_blanc.ligne][cls.pion_fantome_blanc.colonne].piece = None
            cls.pion_fantome_blanc = None

        if case_courante.piece.couleur == BLANC and cls.pion_fantome_noir is not None:
            plateau[cls.pion_fantome_noir.ligne][cls.pion_fantome_noir.colonne].piece = None
            cls.pion_fantome_noir = None

        # Gestion du roque
        if type(piece) == Roi and abs(case_courante.colonne - nouvelle_case.colonne) > 1:
            if case_courante.colonne - nouvelle_case.colonne == -2:
                # Petit Roque
                ligne = 7 if piece.couleur == BLANC else 0
                tour = plateau[ligne][7].piece
                plateau[ligne][7].piece.colonne -= 2
                plateau[ligne][5].piece = tour
                plateau[ligne][7].piece = None
            else:
                # Grand Roque
                ligne = 7 if piece.couleur == BLANC else 0
                tour = plateau[ligne][0].piece
                plateau[ligne][0].piece.colonne += 3
                plateau[ligne][3].piece = tour
                plateau[ligne][0].piece = None

        piece.ligne, piece.colonne = nouvelle_case.ligne, nouvelle_case.colonne
        if nouvelle_case.piece is not None:
            cls.nb_coups_sans_prise = 0

        nouvelle_case.piece = piece
        case_courante.piece = None

        piece.a_bouge = True

        # Promotion du pion
        if type(piece) == Pion:
            if piece.ligne == 0 or piece.ligne == 7:
                affichage_promotion_pion()
                piece.promotion(plateau)

        # Alerte si l'adversaire est en échec
        toutes_positions_attaque = []
        position_roi_adverse = (-1, -1)
        joueur_adverse = NOIR if piece.couleur == BLANC else BLANC
        for ligne in plateau:
            for cell in ligne:
                if cell.piece is not None:
                    if cell.piece.couleur != piece.couleur:
                        if type(cell.piece) == Roi:
                            position_roi_adverse = (
                                cell.piece.ligne,
                                cell.piece.colonne,
                            )
                            logging.debug("[Alerte]: Roi adverse trouvé")
                            logging.debug(
                                f"[Position du Roi adverse]: {position_roi_adverse}"
                            )
                    else:
                        positions = cell.piece.chercheTousLesDeplacements(echiquier)
                        if len(positions):
                            toutes_positions_attaque.extend(positions)

        if position_roi_adverse in toutes_positions_attaque:
            logging.debug("[Alerte]: ECHEC !")
            echiquier.echec_en_cours = joueur_adverse
            echiquier.echec_alerte = True
            return

        echiquier.echec_en_cours = None

        # Implémente les parties nulles:
        # 2 cas: 50 coups sont prises de pièces ou bien 3 fois la même situation
        if cls.nb_coups_sans_prise > 50:
            echiquier.partie_nulle = True

        cls.verifie_position_nulle(echiquier)
        cls.memorise(echiquier)

        # movement_sound = (
        #     pygame.mixer.Sound("Assets/music/capture.wav")
        #     if capture
        #     else pygame.mixer.Sound("Assets/music/move.wav")
        # )
        # movement_sound.play()


    @classmethod
    def verifie_position_nulle(cls, echiquier):
        trouve = 0
        echiquier_courant = [case_echiquier.piece for ligne in echiquier.cases_echiquier for case_echiquier in ligne]
        for position in cls.historique_positions:
            if position == echiquier_courant:
                trouve += 1

        if trouve == 2:
            echiquier.partie_nulle = True


    @classmethod
    def memorise(cls, echiquier):
        echiquier_courant = [case_echiquier.piece for ligne in echiquier.cases_echiquier for case_echiquier in ligne]
        cls.historique_positions.append(echiquier_courant)

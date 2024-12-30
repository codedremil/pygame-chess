import logging
import sys
import pygame
from pygame import mixer
from echiquier import Echiquier
from ihm import TAILLE_PLATEAU
from ihm import initialise_jeu, affiche_jeu, ecran_fin_de_jeu, redemarre_jeu

TEMPS_PAR_JOUEUR = 300

logging.basicConfig(level=logging.INFO)
pygame.init()
pygame.font.init()
#mixer.init()

def main():
    fenetre = initialise_jeu()
    clock = pygame.time.Clock()
    plateau = Echiquier(TAILLE_PLATEAU, TEMPS_PAR_JOUEUR, jeu_initial)
    counter = 0
    run = True
    while run:
        clock.tick(10)
        affiche_jeu(fenetre, plateau)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = plateau.determineLaCase(pygame.mouse.get_pos())
                if event.button == 1:
                    plateau.selectionneLaCase(cell)
                if event.button == 3:
                    plateau.deselectionneLaCase()
            if event.type == pygame.KEYDOWN:
                if plateau.gagnant is not None or plateau.partie_nulle or event.key == pygame.K_SPACE:
                    redemarre_jeu(fenetre)
                    return

        if plateau.gagnant is not None:
            if not counter:
                #game_finish_sound = pygame.mixer.Sound("Assets/music/Game_Finish.wav")
                #game_finish_sound.play()
                counter = not counter
            ecran_fin_de_jeu(fenetre, plateau, plateau.gagnant)
            return

        if plateau.partie_nulle:
            plateau.dessine(fenetre)
            ecran_fin_de_jeu(fenetre, plateau, "NUL")
            return

        #affiche_jeu(fenetre, plateau)


if __name__ == "__main__":
    # Test du PAT
    test_pat = {
        'tour': 'blanc',
        'pieces': ["ra8", "Pa7", "Rc6"],
    }
    # Test échec et mat
    test_echec_et_mat = {
        'tour': 'blanc',
        'pieces': ["ra8", "Pa7", "Ra6", "Fc4"]
    }
    # Test promotion du pion blanc
    test_promotion_blanc = {
        'tour': 'blanc',
        'pieces': ["ra8", "Pa7", "Rc4", "Pf7"],
    }
    # Test partie nulle
    test_partie_nulle = {
        'tour': 'noir',
        'pieces': ["re8", "Re6"]
    }
    # Test echec decouverte
    test_echec_decouverte = {
        'tour': 'noir',
        'pieces': ["re8", "te7", "Te2", "Re1"]
    }
    #jeu_initial = test_pat
    #jeu_initial = test_echec_et_mat
    #jeu_initial = test_promotion_blanc
    #jeu_initial = test_partie_nulle
    #jeu_initial = test_echec_decouverte
    jeu_initial = None
    while True:
        main()

# EOF
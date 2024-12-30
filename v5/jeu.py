import pygame
from pygame import mixer
from echiquier import Echiquier
from ihm import TAILLE_PLATEAU
from ihm import initialise_jeu, affiche_jeu, ecran_fin_de_jeu

TEMPS_PAR_JOUEUR = 1

pygame.init()
pygame.font.init()
#mixer.init()

def main():
    fenetre = initialise_jeu()
    clock = pygame.time.Clock()
    # part5: jeu_initial
    #plateau = Echiquier(TAILLE_PLATEAU, TEMPS_PAR_JOUEUR)
    plateau = Echiquier(TAILLE_PLATEAU, TEMPS_PAR_JOUEUR, jeu_initial)
    counter = 0
    run = True
    while run:
        affiche_jeu(fenetre, plateau)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit(0)

            # v4/1 prise en compte de la sélection de la pièce
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = plateau.determineLaCase(pygame.mouse.get_pos())
                if event.button == 1:
                    plateau.selectionneLaCase(cell)
                if event.button == 3:
                    plateau.deselectionneLaCase()

        # part5/2: ajout des tests de fins de jeu
        if plateau.gagnant is not None:
            if not counter:
                #game_finish_sound = pygame.mixer.Sound("Assets/music/Game_Finish.wav")
                #game_finish_sound.play()
                counter = not counter
            ecran_fin_de_jeu(fenetre, plateau, plateau.gagnant)
            return

        # part5/2
        if plateau.partie_nulle:
            plateau.dessine(fenetre)
            ecran_fin_de_jeu(fenetre, plateau, "NUL")
            return

if __name__ == "__main__":
    # Test échec et mat
    test_echec_et_mat = {
        'tour': 'blanc',
        'pieces': ["ra8", "Pa7", "Ra6", "Fc4"]
    }
    jeu_initial = test_echec_et_mat
    jeu_initial = None
    while True:
        main()

# EOF
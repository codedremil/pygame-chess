import pygame
from piece import BLANC, NOIR

LARGEUR, HAUTEUR = (1000, 600)
TAILLE_CASE = 70
TAILLE_PLATEAU = 8 * TAILLE_CASE
COULEUR_FOND = (35, 35, 35)
COULEUR_BORD = (100, 149, 237)


def initialise_jeu():
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Jeu d'échec")
    return fenetre


def affiche_jeu(fenetre, plateau):
    fenetre.fill(COULEUR_FOND)
    pygame.draw.rect(fenetre, COULEUR_BORD, (0, 0, HAUTEUR, HAUTEUR))   # carré de l'échiquier
    plateau.dessine(fenetre)
    pygame.display.update()


def affiche_message_centre(fenetre, taille_fonte, message, couleur=(255, 0 ,0), hauteur=HAUTEUR // 2 - 20):
    fonte = pygame.font.SysFont("Sans Serif", taille_fonte)
    text = fonte.render(message, False, couleur)
    largeur, _ = fonte.size(message)
    fenetre.blit(text, (560 + (LARGEUR - TAILLE_PLATEAU - largeur) // 2 + 20, hauteur))

# v4/3
def ecran_fin_de_jeu(fenetre, plateau, vainqueur):
    pygame.draw.rect(fenetre, (35, 35, 35), (601, 0, LARGEUR - TAILLE_PLATEAU, HAUTEUR))
    affiche_message_centre(fenetre, 30, "Appuyez sur une touche", (255, 255, 255), 10)

    if plateau.partie_nulle:
        affiche_message_centre(fenetre, 50, "Partie nulle !", (255, 0, 0), 100)
    elif vainqueur == "PAT":
        affiche_message_centre(fenetre, 50, "PAT !")
    else:
        raison_victoire= "Echec et mat !" if plateau.raison_victoire == "MAT" else "Temps écoulé !"
        message = "Les Blancs gagnent !" if vainqueur == BLANC else "Les Noirs gagnent !"
        affiche_message_centre(fenetre, 50, raison_victoire, (255, 0, 0), 100)
        affiche_message_centre(fenetre, 50, message, (255, 0, 0))

    pygame.display.update()

# v4/3
def redemarre_jeu(fenetre):
    fenetre.fill((35, 35, 35))
    affiche_message_centre(fenetre, 60, "Réinitialisation...")
    pygame.display.update()
    pygame.time.delay(3000)
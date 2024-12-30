from piece import BLANC, NOIR
from ihm import affiche_message_centre
import pygame

# pygame.font.init()
# font = pygame.font.SysFont("Sans Serif", 30)


class Joueur:
    def __init__(self, couleur, temps_initial):
        self.couleur = couleur
        self.time = temps_initial #* 60  # conversion en secondes
        if self.couleur == BLANC:
            self.a_le_trait = True
        else:
            self.a_le_trait = False

        self.clock_tick = 0
        self.time_over = False  # semble inutile

    def inverseLeTour(self):
        self.a_le_trait = not self.a_le_trait

    def afficheTempsRestant(self, fenetre):
        """
        Calcule et affiche le temps restant pour le joueur
        """
        if self.a_le_trait:
            self.clock_tick += 1
            if self.clock_tick >= 10:
                self.clock_tick = 0
                seconds = self.time - 1
                self.time -= 1
            else:
                seconds = self.time
        else:
            seconds = self.time

        if self.time <= 0:  # player looses if his time is over
            self.time_over = True

        minutes = seconds // 60
        seconds -= minutes * 60
        if minutes < 1:
            minutes = "00"
        elif minutes < 10:
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)

        if seconds < 1:
            seconds = "00"
        elif seconds < 10:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)

        # text = font.render(
        #     f"Temps restant: {minutes}:{seconds}", False, (255, 255, 255)
        # )
        # fenetre.blit(text, (position[0], position[1]))
        affiche_message_centre(fenetre, 30, f"Temps restant: {minutes}:{seconds}", (255, 255, 255), 10 if self.couleur == NOIR else 570)

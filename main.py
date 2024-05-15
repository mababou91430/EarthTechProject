import pygame

from fonction import *
from pygame import *
import sys

num_image = 0

# Initialisation de Pygame
pygame.init()
pygame.font.init()
test = afficher_image(num_image)

# Boucle principale du jeu
running = True
init = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            num_image += 1
            test.__next__(num_image)
            #mouse_pos = pygame.mouse.get_pos()
            #if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[
                #1] <= button_y + button_height:
                #print("Bouton cliqué !")  # Action à effectuer lorsque le bouton est cliqué
                #running = False
        elif init:
            test.__init__(num_image)
            init = False

    # Affichage de l'image de fond


    # Rafraîchissement de l'écran
    pygame.display.update()

# Quitter Pygame
pygame.font.quit()
pygame.quit()
sys.exit()


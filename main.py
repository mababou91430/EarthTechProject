import pygame

from fonction import *
from pygame import *
import sys

num_image = 0
menu = 0

# Initialisation de Pygame
pygame.init()
pygame.font.init()
test = afficher_image(num_image)
menu_option = ["Son  Retour  Quitter"]
menu_accueil = bouton(menu_option)

# Boucle principale du jeu
running = True
init = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            #num_image += 1
            #test.__next__(num_image)
            menu = menu_accueil.bouton_clicker(menu_accueil, mouse_pos[0],mouse_pos[1],num_image,menu)

        elif init:
            menu_accueil.__init__(menu_option)
            test.__init__(num_image)
            init = False
            menu_accueil.accueil()


    # Affichage de l'image de fond


    # Rafraîchissement de l'écran
    pygame.display.update()

# Quitter Pygame
pygame.font.quit()
pygame.quit()
sys.exit()


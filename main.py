import pygame

from fonction import *
from pygame import *
import sys

num_image = 0
menu = 0
curseur_saisie = False

window = pygame.display.set_mode((window_width, window_height))

# Initialisation de Pygame
pygame.init()
pygame.font.init()
test = afficher_image(num_image)
menu_option = ["                     Retour               Quitter"]
menu_accueil = bouton(menu_option)
pygame.mixer.init()
pygame.mixer.music.load('musique/Biome foret.mp3')
pygame.mixer.music.play(-1)


# Boucle principale du jeu
running = True
init = True
choix_incrementation = [[0, 0, 0, 0, 0], [0]] #[[foret, desert, eau, glace, tempo 1], [incrementation]]
volume_defaut = 0.5
volume_slider = Slider(180, 240, 100, 20, 0, 1, 0.01, volume_defaut)

pygame.mixer.music.set_volume(volume_defaut)

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if not(num_image in [0, 5, 26, 33, 48, 54, 55, 59, 64, 67, 74, 82, 89, 92]):
                choix_incrementation = image_incrementation(num_image, choix_incrementation)
                num_image += choix_incrementation[1]
                if num_image != 0:
                    test.__next__(num_image)
                else:
                    init = 1
            elif num_image != 0:
                choix_incrementation = choice_selection(num_image,mouse_pos,choix_incrementation)
                num_image += choix_incrementation[1]
                test.__next__(num_image)
            if pygame.MOUSEBUTTONUP:
                menu = menu_accueil.bouton_clicker(menu_accueil, mouse_pos[0], mouse_pos[1], num_image, menu, rect)
        if menu == 2:
            running = False
        elif menu == 1:
            menu_accueil.draw(window, rect)
            volume_slider.handle_event(event)
            volume_slider.draw(window)
            font = pygame.font.Font(None, 36)
            pygame.draw.rect(window,GRAY,(160,200,150,25))
            text = font.render(f'Volume: {int(volume_slider.get_value()*100)}', True, BLACK)
            window.blit(text, (165, 200))
            pygame.mixer.music.set_volume(volume_slider.get_value())

        elif menu == 3:
            num_image += 1
            test.__next__(num_image)
            menu = 0
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


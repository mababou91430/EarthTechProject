import pygame
pygame.init()
pygame.font.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150,150,150)
image = 'Image.txt'
class afficher_image:

    def __init__(self):
        window_width = 1020
        window_height = 1020

        # Création de la fenêtre
        window = pygame.display.set_mode((window_width, window_height))
        with open(image,"r") as image_set :
            ligne = image_set.readline()
            print(ligne)
            background_image = pygame.image.load(ligne).convert()
            background_image = pygame.transform.scale(background_image, (window_width, window_height))
            window.blit(background_image, (0, 0))


    #def __next__(v):

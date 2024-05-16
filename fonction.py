import pygame
import sys

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
image = 'EarthTechProject/Image.txt'
window_width = 1020
window_height = 1020

font = pygame.font.SysFont(None, 36)

# Création de la fenêtre
window = pygame.display.set_mode((window_width, window_height))
with open(image, "r") as image_set:
    ligne = image_set.readlines()
    tab_image = ligne[0].split(" ")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

class afficher_image:

    def __init__(self, num_image):

        background_image = pygame.image.load(tab_image[num_image]).convert()
        background_image = pygame.transform.scale(background_image, (window_width, window_height))
        window.blit(background_image, (0, 0))

    def __next__(self, num_image):
        background_image = pygame.image.load(tab_image[num_image]).convert()
        background_image = pygame.transform.scale(background_image, (window_width, window_height))
        window.blit(background_image, (0, 0))

bouton_exit = 'EarthTechProject/Image/Exit.png'

taille_bouton_x = 126
taille_bouton_y = 50

pos_bouton_x = (window_width - taille_bouton_x) // 2
pos_bouton_y = window_height - 250

class bouton:

    def __init__(self, items):
        self.items = items

    def accueil(self):
        bouton_exit_image = pygame.image.load(bouton_exit).convert()
        bouton_exit_image = pygame.transform.scale(bouton_exit_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_exit_image, (pos_bouton_x+150, pos_bouton_y))
        bouton_option_image = pygame.image.load(bouton_exit).convert()
        bouton_option_image = pygame.transform.scale(bouton_option_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_option_image, (pos_bouton_x, pos_bouton_y))
        bouton_start_image = pygame.image.load(bouton_exit).convert()
        bouton_start_image = pygame.transform.scale(bouton_start_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_start_image, (pos_bouton_x-150, pos_bouton_y))


    def draw(self, surface):
        for index, item in enumerate(self.items):
            draw_text(item, font, BLACK, surface, 50, 200 + index*50)

    def bouton_clicker(self,menu_accueil, x, y):
        if 50 <= x <= 150 and 50 <= y <= 100:
                menu_accueil.draw(window)
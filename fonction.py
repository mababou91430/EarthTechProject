import pygame
import pygame.mixer

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 128)
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


volume = 50
pygame.mixer.music.set_volume(volume / 100)

def dessiner_curseur(rect):
    pygame.draw.rect(window, GRAY, rect)
    pygame.draw.rect(window, WHITE,(window.x, window.y, window.width * (volume / 100), window.height))

def draw_text(text, font, color, surface, x, y):
    pygame.draw.rect(surface, GRAY, (x-5-90, y, 55, 25))
    pygame.draw.rect(surface, GRAY, (x+55, y, 85, 25))
    pygame.draw.rect(surface, GRAY, (x+145+90, y, 100, 25))
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x-90, y)
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
            pygame.draw.rect(surface, (255, 0, 0, 128), (255, (200 + index*50)-10, (window_width + index*50)//2, 200 + index*50))
            draw_text(item, font, BLACK, surface, ((window_width//2)-120), 200 + index*50)

    def bouton_clicker(self, menu_accueil, x, y, num_image, menu1):
        print(num_image, " , ", x, " , ", y, " , ", menu1)
        if (num_image == 0 and pos_bouton_x <= x <= pos_bouton_x+150 and pos_bouton_y <= y <= pos_bouton_y+50
                and menu1 == 0):
            menu_accueil.draw(window)
            menu1 += 1
            print("test2")
            return menu1
        elif num_image == 0 and menu1 == 1 and 445 <= x <= 530 and 200 <= y <= 200+25:
            print("test1")
            afficher_image.__init__(self, 0)
            bouton.accueil(self)
            menu1 -= 1
            return menu1
        elif num_image == 0 and menu1 == 1 and 625 <= x <= 725 and 200 <= y <= 225:
            return 2
        else:
            if menu1 == 1:
                return 1
            else:
                return 0

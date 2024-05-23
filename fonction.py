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

def draw(self, surface):
    pygame.draw.rect(surface, (169, 169, 169), self.rect)
    pygame.draw.rect(surface, (255, 0, 0), self.knob_rect)

def get_volume(self):
    return self.volume / 100


def draw_text(text, font, color, surface, x, y, rect):
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

class Slider:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.knob_rect = pygame.Rect(x, y, 20, height)  # Taille fixe du knob

    def draw(self, background_image):
        pygame.draw.rect(background_image, (200, 200, 200), self.rect)  # Le fond du slider
        pygame.draw.rect(background_image, (100, 100, 250), self.knob_rect)  # Le knob
        self.draw(background_image)

    def update_knob_position(self, mouse_x):
        self.knob_rect.x = max(self.rect.x, min(mouse_x, self.rect.x + self.rect.width - self.knob_rect.width))

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

    def draw(self, surface, rect):
        for index, item in enumerate(self.items):
            pygame.draw.rect(surface, (255, 0, 0, 128), (255, (200 + index*50)-10, (window_width + index*50)//2, 200 + index*50))
            draw_text(item, font, BLACK, surface, ((window_width//2)-120), 200 + index*50, rect)

    def bouton_clicker(self, menu_accueil, x, y, num_image, menu1, rect):
        print(num_image, " , ", x, " , ", y, " , ", menu1)
        if (num_image == 0 and pos_bouton_x <= x <= 575 and pos_bouton_y <= y <= pos_bouton_y+50
                and menu1 == 0):
            menu_accueil.draw(window, rect)
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
        elif num_image == 0 and menu1 == 0 and 600 <= x <= 725 and 770 <= y <= 800:
            return 2
        elif num_image == 0 and menu1 == 0 and 300 <= x <= 420 and 770 <= y <= 800:
            return 3
        #elif num_image == 0 and menu1 == 1 and 275 <= x <= 375 and 250 <= y <= 270:



        else:
            if menu1 == 1:
                return 1
            else:
                return 0



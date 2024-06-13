import pygame
import pygame.mixer

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 128)
GRAY = (150, 150, 150)
RED = (255,0,0)
image = 'Image.txt'
window_width = 800
window_height = 1020

font = pygame.font.SysFont(None, 36)

# Création de la fenêtre
window = pygame.display.set_mode((window_width, window_height))

with open(image, "r") as image_set:
    ligne = image_set.readlines()
    tab_image = ligne[0].split(" ")


def draw_text(text, font, color, surface, x, y, rect):
    pygame.draw.rect(surface, GRAY, (x + 55, y, 85, 25))
    pygame.draw.rect(surface, GRAY, (x + 145 + 90, y, 100, 25))
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x - 90, y)
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


bouton_exit = 'Image/Exit.png'
bouton_start = 'Image/start.png'
bouton_option = 'Image/option.png'

taille_bouton_x = 126
taille_bouton_y = 50

pos_bouton_x = (window_width - taille_bouton_x) // 2
pos_bouton_y = window_height - 250

etat_musique = 1

class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, step, default_val):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.step = step
        self.value = default_val
        self.handle_rect = pygame.Rect(x + int((default_val - min_val) / (max_val - min_val) * (w - w // 20)), y, w // 20, h)
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)
        pygame.draw.rect(screen, WHITE, self.handle_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.handle_rect.x = max(self.rect.x, min(event.pos[0] - self.handle_rect.width // 2, self.rect.x + self.rect.width - self.handle_rect.width))
                self.value = self.min_val + ((self.handle_rect.x - self.rect.x) / (self.rect.width - self.handle_rect.width)) * (self.max_val - self.min_val)
                self.value = round(self.value / self.step) * self.step  # Arrondir à la valeur la plus proche du pas

    def get_value(self):
        return self.value

class bouton:

    def __init__(self, items):
        self.items = items

    def accueil(self):
        bouton_exit_image = pygame.image.load(bouton_exit).convert()
        bouton_exit_image = pygame.transform.scale(bouton_exit_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_exit_image, (pos_bouton_x + 150, pos_bouton_y))
        bouton_option_image = pygame.image.load(bouton_option).convert()
        bouton_option_image = pygame.transform.scale(bouton_option_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_option_image, (pos_bouton_x, pos_bouton_y))
        bouton_start_image = pygame.image.load(bouton_start).convert()
        bouton_start_image = pygame.transform.scale(bouton_start_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_start_image, (pos_bouton_x - 150, pos_bouton_y))

    def draw(self, surface, rect):
        for index, item in enumerate(self.items):
            pygame.draw.rect(surface, (255, 0, 0, 128),
                             (150, 200-15, 500, 200 + index * 50))
            draw_text(item, font, BLACK, surface, ((window_width // 2) - 120), 200 + index * 50, rect)

    def bouton_clicker(self, menu_accueil, x, y, num_image, menu1, rect):
        print(num_image, " , ", x, " , ", y, " , ", menu1)
        if (num_image == 0 and pos_bouton_x <= x <= 465 and pos_bouton_y <= y <= pos_bouton_y + 50
                and menu1 == 0):
            menu_accueil.draw(window, rect)
            menu1 += 1
            print("test2")
            return menu1
        elif menu1 == 1 and 349 <= x <= 416 and 200 <= y <= 200 + 25:
            print("test1")
            afficher_image.__init__(self, num_image)
            if num_image == 0:
                bouton.accueil(self)
            menu1 -= 1
            return 4
        elif menu1 == 1 and 490 <= x <= 569 and 200 <= y <= 225:
            return 2
        elif num_image == 0 and menu1 == 0 and 485 <= x <= 615 and 770 <= y <= 825:
            return 2
        elif num_image == 0 and menu1 == 0 and 180 <= x <= 315 and 770 <= y <= 825:
            return 3
        else:
            if menu1 == 1:
                return 1
            else:
                return 0


def choice_selection(num_image, mouse_pos, choix_incrementation):
    if num_image in [5, 26, 33, 47, 53, 56, 61, 64] and mouse_pos[0] < 400 and mouse_pos[1] >= 800:
        if num_image == 33:  # pouvoir foret
            choix_incrementation[0][0] = 1
        choix_incrementation[1] = 1
    elif num_image in [52] and mouse_pos[0] < 400 and mouse_pos[1] >= 800:
        choix_incrementation[1] = 2
    elif (num_image in [5, 26, 33, 47] or (num_image in [61, 64] and choix_incrementation[0][0])) and 400 <= mouse_pos[0] and mouse_pos[1] >= 800:
        if num_image in [5]:
            choix_incrementation[0][-1] = 1
        choix_incrementation[1] = 2
    elif num_image in [52, 53, 56] and 400 <= mouse_pos[0] and mouse_pos[1] >= 800:  # choix partir seul
        choix_incrementation[1] = 58 - num_image
    else:
        choix_incrementation[1] = 0
    return choix_incrementation


def image_incrementation(num_image, choix_incrementation):
    if num_image == 44:
        pygame.mixer.music.load('musique/Biome desert.mp3')
        pygame.mixer.music.play(-1)
    if num_image in [6, 27, 34, 35, 36, 37, 38, 48, 49, 50, 51, 57, 58, 59]:
        choix_incrementation[1] = 2
    elif num_image in []:
        choix_incrementation[1] = 3
    elif num_image in [12, 60, 63] or (num_image in [9] and choix_incrementation[0][-1]):
        choix_incrementation[1] = 4
    elif num_image in [39, 62]:
        choix_incrementation[1] = 5
    elif num_image == 65:
        choix_incrementation[1] = -20
    elif num_image == 69:
        choix_incrementation[1] = num_image * -1
        pygame.mixer.music.load('musique/Biome foret.mp3')
        pygame.mixer.music.play(-1)
        choix_incrementation[0] = [0, 0, 0, 0, 0]
    else:
        choix_incrementation[1] = 1
    return choix_incrementation

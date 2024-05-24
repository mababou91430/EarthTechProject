import pygame
import pygame.mixer

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 128)
GRAY = (150, 150, 150)
image = 'Image.txt'
window_width = 1020
window_height = 1020

font = pygame.font.SysFont(None, 36)

# Création de la fenêtre
window = pygame.display.set_mode((window_width, window_height))

with open(image, "r") as image_set:
    ligne = image_set.readlines()
    tab_image = ligne[0].split(" ")


class Game:
    def __init__(self):
        self.screen = window
        self.clock = pygame.time.Clock()
        self.running = True

        # Charger la musique
        self.music_path = "musique/Falling In Reverse - Ronald.mp3"
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)  # Joue la musique en boucle

        # Créer le curseur de volume
        self.volume_slider = VolumeSlider(275, 250, 100, 20)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.volume_slider.handle_event(event)

        # Mettre à jour le volume de la musique
        pygame.mixer.music.set_volume(self.volume_slider.get_volume())

        # Dessiner
        self.volume_slider.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)


class VolumeSlider:
    def __init__(self, x, y, width, height, initial_volume=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.volume = initial_volume
        self.knob_rect = pygame.Rect(x + (initial_volume / 100) * width, y, 10, height)
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.knob_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.knob_rect.x = min(max(self.rect.x, event.pos[0]),
                                       self.rect.x + self.rect.width - self.knob_rect.width)
                self.volume = ((self.knob_rect.x - self.rect.x) / self.rect.width) * 100

    def draw(self, surface):
        pygame.draw.rect(surface, (169, 169, 169), self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.knob_rect)

def get_volume(self):
    return self.volume / 100


def draw_text(text, font, color, surface, x, y, rect):
    pygame.draw.rect(surface, GRAY, (x - 5 - 90, y, 55, 25))
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

bouton_exit = 'Image/Exit.png'

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
        window.blit(bouton_exit_image, (pos_bouton_x + 150, pos_bouton_y))
        bouton_option_image = pygame.image.load(bouton_exit).convert()
        bouton_option_image = pygame.transform.scale(bouton_option_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_option_image, (pos_bouton_x, pos_bouton_y))
        bouton_start_image = pygame.image.load(bouton_exit).convert()
        bouton_start_image = pygame.transform.scale(bouton_start_image, (taille_bouton_x, taille_bouton_y))
        window.blit(bouton_start_image, (pos_bouton_x - 150, pos_bouton_y))

    def draw(self, surface, rect):
        for index, item in enumerate(self.items):
            pygame.draw.rect(surface, (255, 0, 0, 128),
                             (255, (200 + index * 50) - 10, (window_width + index * 50) // 2, 200 + index * 50))
            draw_text(item, font, BLACK, surface, ((window_width // 2) - 120), 200 + index * 50, rect)
            pygame.draw.rect(surface,(0,0,0),(300,250,50,50))

    def bouton_clicker(self, menu_accueil, x, y, num_image, menu1, rect):
        print(num_image, " , ", x, " , ", y, " , ", menu1)
        if (num_image == 0 and pos_bouton_x <= x <= 575 and pos_bouton_y <= y <= pos_bouton_y + 50
                and menu1 == 0):
            menu_accueil.draw(window, rect)
            menu1 += 1
            print("test2")
            return menu1
        elif num_image == 0 and menu1 == 1 and 445 <= x <= 530 and 200 <= y <= 200 + 25:
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
        elif num_image == 0 and menu1 == 1 and 300 <= x <= 350 and 250 <= y <= 300:
            pygame.mixer.music.pause()

        else:
            if menu1 == 1:
                return 1
            else:
                return 0


def choice_selection(num_image, mouse_pos):
    if num_image in [3] and 15 <= mouse_pos[0] <= 340 and 440 <= mouse_pos[1] <= 590:
        return 1
    elif num_image in [3] and 615 <= mouse_pos[0] <= 1000 and 425 <= mouse_pos[1] <= 580:
      return 2
    return 0


def image_incrementation(num_image):
    if num_image in [4]:
        return 2
    return 1

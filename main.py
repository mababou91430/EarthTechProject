import pygame
import sys

# Initialisation de Pygame
pygame.init()
pygame.font.init()

# Taille de la fenêtre
window_width = 1020
window_height = 1020

# Création de la fenêtre
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Arrière-plan avec Pygame")

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150,150,150)

button_width = 200
button_height = 150
button_x = (window_width - button_width) // 2
button_y = 700

# Chargement de l'image de fond
background_image = pygame.image.load('EarthTechProject/Accueil.png').convert()

# Redimensionnement de l'image pour qu'elle corresponde à la taille de la fenêtre
background_image = pygame.transform.scale(background_image, (window_width, window_height))

button_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)

font = pygame.font.SysFont('arial',40)

def draw_button(button_surface):
    pygame.draw.rect(button_surface, GRAY, (button_x, button_y, button_width, button_height))
    button_image = pygame.image.load('EarthTechProject/button_image.png')
    button_image = pygame.transform.scale(button_image, (button_width, button_height))
    background_image.blit(button_image, (button_x, button_y))


draw_button(button_surface)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[
                1] <= button_y + button_height:
                print("Bouton cliqué !")  # Action à effectuer lorsque le bouton est cliqué
                running = False

    # Affichage de l'image de fond
    window.blit(background_image, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.update()

# Quitter Pygame
pygame.font.quit()
pygame.quit()
sys.exit()

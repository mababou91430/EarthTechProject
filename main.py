import pygame
import sys

# Initialisation de Pygame
pygame.init()
pygame.font.init()

# Taille de la fenêtre
window_width = 1920
window_height = 1080

# Création de la fenêtre
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Arrière-plan avec Pygame")

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150,150,150)

button_width = 100
button_height = 70
button_x = (window_width - button_width) // 2
button_y = (window_height - button_height) // 2

# Chargement de l'image de fond
background_image = pygame.image.load('EarthTechProject/foretv3.jpg').convert()

# Redimensionnement de l'image pour qu'elle corresponde à la taille de la fenêtre
background_image = pygame.transform.scale(background_image, (window_width, window_height))

font = pygame.font.SysFont('arial',40)

def draw_button():
    pygame.draw.rect(background_image, GRAY, (button_x, button_y, button_width, button_height))
    text = font.render("Quitter", True, BLACK)
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    background_image.blit(text, text_rect)

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

import pygame

class VolumeSlider:
    def __init__(self, x, y, width, height, initial_volume=50):
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
                self.knob_rect.x = min(max(self.rect.x, event.pos[0]), self.rect.x + self.rect.width - self.knob_rect.width)
                self.volume = ((self.knob_rect.x - self.rect.x) / self.rect.width) * 100

    def draw(self, surface):
        pygame.draw.rect(surface, (169, 169, 169), self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.knob_rect)

    def get_volume(self):
        return self.volume / 100

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Contrôle du volume")
        self.clock = pygame.time.Clock()
        self.running = True

        # Charger la musique
        self.music_path = "chemin/vers/votre/musique.mp3"
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)  # Joue la musique en boucle

        # Créer le curseur de volume
        self.volume_slider = VolumeSlider(350, 300, 100, 20)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.volume_slider.handle_event(event)

            # Mettre à jour le volume de la musique
            pygame.mixer.music.set_volume(self.volume_slider.get_volume())

            # Dessiner
            self.screen.fill((255, 255, 255))
            self.volume_slider.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()

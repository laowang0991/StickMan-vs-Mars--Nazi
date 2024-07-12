import pygame

class Background:
    def __init__(self, path, width, height):
        self.background = pygame.image.load("All picture/background.png").convert()
        self.background = pygame.transform.scale(self.background, (width, height))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
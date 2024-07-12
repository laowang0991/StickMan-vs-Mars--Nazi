# death_screen.py

import pygame

class DeathScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.image = pygame.image.load("All picture/You Died.png")

    def show(self):
        x = self.width // 4 - self.image.get_width() // 4
        y = self.height // 6 - self.image.get_height() // 6
        self.screen.blit(self.image, (x, y))

import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Bullet color (red)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, *args):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > pygame.display.get_surface().get_height() or self.rect.right < 0 or self.rect.left > pygame.display.get_surface().get_width():
            self.kill()  # Remove the bullet if it goes off-screen
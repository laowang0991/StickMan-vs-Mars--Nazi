# enemy_bullet.py

import pygame

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y, target=None):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Bullet color (red)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.target = target

    def update(self, *args):
        if self.target:
            dx = self.target.rect.centerx - self.rect.centerx
            dy = self.target.rect.centery - self.rect.centery
            distence = (dx ** 2 + dy ** 2) ** 0.5
            if distence != 0:
                self.speed_x = 5 * (dx / distence)
                self.speed_y = 5 * (dy / distence)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom < 0 or self.rect.top > pygame.display.get_surface().get_height() or self.rect.right < 0 or self.rect.left > pygame.display.get_surface().get_width():
            self.kill()  # Remove the bullet if it goes off-screen

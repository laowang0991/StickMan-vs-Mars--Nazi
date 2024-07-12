import pygame
from weapon import Bullet

class Stickman(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__()
        self.image = pygame.image.load("All picture/Stickman.png").convert_alpha()   # load the image
        self.image = pygame.transform.scale(self.image, (50, 50))         # resize
        self.rect = self.image.get_rect()
        self.rect.center = (1800 // 2, 1600 // 2)
        self.speed = 2
        self.direction = None
        self.health = 10

    def update(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = 'left'
        if keys[pygame.K_d] and self.rect.right < 1800:
            self.rect.x += self.speed
            self.direction = 'right'
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
            self.direction = 'up'
        if keys[pygame.K_s] and self.rect.bottom < 1600:
            self.rect.y += self.speed
            self.direction = 'down'

        # make sure the stickman is always in the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1800:
            self.rect.right = 1800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 1600:
            self.rect.bottom = 1600
        
    def fire(self):
        if self.direction == 'left':
            return Bullet(self.rect.centerx, self.rect.centery, -10, 0)
        elif self.direction == 'right':
            return Bullet(self.rect.centerx, self.rect.centery, 10, 0)
        elif self.direction == 'up':
            return Bullet(self.rect.centerx, self.rect.centery, 0, -10)
        elif self.direction == 'down':
            return Bullet(self.rect.centerx, self.rect.centery, 0, 10)
        else:
            return None  # No direction, do not fire
        
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            return True
        return False
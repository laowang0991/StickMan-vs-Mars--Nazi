import pygame
import random
import math
from enemyWeapon import EnemyBullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, target):
        super().__init__()
        self.image = pygame.image.load("All picture/enemy.png").convert_alpha()  # load the image
        self.image = pygame.transform.scale(self.image, (50, 50))  # change the size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        self.speed = 1
        self.max_health = 10 # initialize the health
        self.health = self.max_health
        self.target = target
        self.bullet_cooldown = 800
        self.last_shot_time = pygame.time.get_ticks()


    def update(self, *args):
        # get the direction of stickman
        target_x, target_y = self.target.rect.center

        # calculate the direction from enemy to stickman
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery

        # calculate the distance
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # normalize the vector and move as the speed
        if distance != 0:
            self.rect.x += self.speed * (dx / distance)
            self.rect.y += self.speed * (dy / distance)

    def fire(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.bullet_cooldown:
            self.last_shot_time = current_time
            health_ratio = self.health / self.max_health

            if health_ratio > 0.75:
                return self.straight_bullet()
            elif health_ratio > 0.5:
                return self.scatter_bullet()
            elif health_ratio > 0.25:
                return self.homing_bullet()
            elif health_ratio >0:
                return self.wave_bullet()
            elif health_ratio == 0:
                return []
        return None
    
    def straight_bullet(self):
        bullet_speed = 5
        dx = self.target.rect.centerx - self.rect.centerx
        dy = self.target.rect.centery - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance != 0:
            speed_x = bullet_speed * (dx / distance)
            speed_y = bullet_speed * (dy / distance)
            return [EnemyBullet(self.rect.centerx, self.rect.centery, speed_x, speed_y)]
        return []
    
    def scatter_bullet(self):  
        bullet_speed = 5
        bullets = []
        for i in range(-31, 31, 15):
            angle = i * random.uniform(0.1, 0.5)
            speed_x = bullet_speed  * math.cos(angle)
            speed_y = bullet_speed  * math.sin(angle)
            bullets.append(EnemyBullet(self.rect.centerx, self.rect.centery, speed_x, speed_y))
        return bullets
    
    def homing_bullet(self):
        bullet_speed = 3
        dx = self.target.rect.centerx - self.rect.centerx
        dy = self.target.rect.centery - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance != 0:
            speed_x = bullet_speed * (dx / distance)
            speed_y = bullet_speed * (dy / distance)
            return [EnemyBullet(self.rect.centerx, self.rect.centery, speed_x, speed_y, self.target)]
        return []
    
    def wave_bullet(self):
        bullet_speed = 5
        bullets = []
        for i in range(-2, 3):
            angle = i * random.uniform(0.1, 0.5)
            speed_x = bullet_speed * math.cos(angle)
            speed_y = bullet_speed * math.sin(angle)
            bullets.append(EnemyBullet(self.rect.centerx, self.rect.centery, speed_x, speed_y))
        return bullets

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            return True
        return False


import pygame
import sys
import random
from stickman import Stickman
from background import Background
from enemy import Enemy
from weapon import Bullet
from enemyWeapon import EnemyBullet
from death_screen import DeathScreen

# initialize pygame
pygame.init()

# set up the window
WIDTH, HEIGHT = 1800, 1600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("StickMan vs Mars' Nazi")

# create the role's group
stickman = Stickman(WIDTH, HEIGHT)
all_sprites = pygame.sprite.Group()
all_sprites.add(stickman)

# create the background
background = Background("All picture/background.pngd", WIDTH, HEIGHT)

# create the enemy in random time
enemies = pygame.sprite.Group()

# Create an enemy instance and add it to the all_sprites group
enemy = Enemy(WIDTH, HEIGHT, stickman)
all_sprites.add(enemy)

# create a group for bullets
bullets = pygame.sprite.Group()

# create a group for enemy bullets
enemy_bullets = pygame.sprite.Group()

# create a group for death screen
death_screen = DeathScreen(screen, WIDTH, HEIGHT)

# set up the main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_j:  # Change from spacebar to "j" key
                bullet = stickman.fire()
                if bullet:
                   # print(f"bullry fired at({bullet.rect.centerx}, {bullet.rect.centery})")
                    all_sprites.add(bullet)
                    bullets.add(bullet)
    if stickman.health > 0:
        # get the key pressed
        keys = pygame.key.get_pressed()

        # check collide
        # bullets destory the enemies
        hits = pygame.sprite.spritecollide(enemy, bullets, True)
        if hits:
            for enemy_hit in hits:
                enemy.take_damage(1)    # reduce the health by 1
        
        # Enemy fires bullets
        enemy_bullet = enemy.fire()
        if enemy_bullet:
            all_sprites.add(enemy_bullet)
            enemy_bullets.add(enemy_bullet)

        # enemy bullets destory the stickman
        hits_1 = pygame.sprite.spritecollide(stickman, enemy_bullets, True)
        if hits_1:
            for stickman_hit in hits_1:
                stickman.take_damage(1)    # reduce the health by 1

        # draw the background
        background.draw(screen)

        #undate the position of the stickman
        all_sprites.update(keys)

        # draw all roles
        all_sprites.draw(screen)
    else:
        # draw the death screen
        death_screen.show()

    # update the screen
    pygame.display.flip()

# quit the game
pygame.quit()
sys.exit()



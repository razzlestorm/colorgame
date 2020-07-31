import pygame
from player import Player
from spritesheet_functions import SpriteSheet

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

# Initializing pygame
pygame.init()


# clock to maintain speed at 30fps
clock = pygame.time.Clock()


# Defining constants for screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create screen object, takes a tuple, apparently
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

my_spritesheet = SpriteSheet('star-ovr.png')
hero1 = my_spritesheet.get_sprite(0, 0, 31, 47)

canvas.fill((255, 255, 255))
canvas.blit(hero1, (0, SCREEN_HEIGHT-300))
screen.blit(canvas, (0, 0))
pygame.display.update()


# Instatiating Player
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Variable to keep main loop running
running = True

# Main loop
while running:
    # Get all keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT:
                player.go_left()
            if event.key == K_RIGHT:
                player.go_right()
            if event.key == K_UP:
                player.go_up()
            if event.key == K_DOWN:
                player.go_down()
        if event.type == KEYUP:
            if event.key == K_LEFT and player.change_x < 0:
                player.stop_x(pressed_keys)
            if event.key == K_RIGHT and player.change_x > 0:
                player.stop_x(pressed_keys)
            if event.key == K_UP and player.change_y < 0:
                player.stop_y(pressed_keys)
            if event.key == K_DOWN and player.change_y > 0:
                player.stop_y(pressed_keys)
        elif event.type == QUIT:
            running = False



    # update player sprite with keypresses
    player.update(pressed_keys)




# fills screen with black
    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)


# screen.blit(player.surf, player.rect)
    pygame.display.flip()

    clock.tick(30)

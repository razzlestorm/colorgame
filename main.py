import pygame
from player import Player

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Instatiating Player
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Variable to keep main loop running
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


    # Get all keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    # update player sprite with keypresses
    player.update(pressed_keys)
    # update enemy position


# fills screen with black
    screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


# screen.blit(player.surf, player.rect)
    pygame.display.flip()

    clock.tick(30)

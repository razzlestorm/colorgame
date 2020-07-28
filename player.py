import pygame
from spritesheet_functions import SpriteSheet


# Importing pygame.locals for easier access to key coordinates
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


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """


    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("star-ovr.png")
        # Load all the left facing images into a list
        image = sprite_sheet.get_sprite(40, 0, 31, 47)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_sprite(76, 0, 31, 47)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_sprite(112, 0, 31, 47)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_sprite(148, 0, 31, 47)
        self.walking_frames_l.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_sprite(40, 0, 31, 47)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_sprite(76, 0, 31, 47)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_sprite(112, 0, 31, 47)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_sprite(148, 0, 31, 47)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        """ Move the player. """

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

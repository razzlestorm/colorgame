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
        self.walking_frames_d = []
        self.walking_frames_u = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("sprites/star-ovr.png")
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

        # Load all the downward facing images into a list
        image = sprite_sheet.get_sprite(40, 56, 31, 47)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_sprite(76, 56, 31, 47)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_sprite(112, 56, 31, 47)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_sprite(148, 56, 31, 47)
        self.walking_frames_d.append(image)


        # Load all the upward images into a list
        image = sprite_sheet.get_sprite(40, 112, 31, 47)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_sprite(76, 112, 31, 47)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_sprite(112, 112, 31, 47)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_sprite(148, 112, 31, 47)
        self.walking_frames_u.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(self, pressed_keys):
        """ Move the player. """

        # Move left/right
        self.rect.x += self.change_x
        self.rect.y += self.change_y


        if self.direction == "R":
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # Move up/down
        elif self.direction == "U":
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        elif self.direction == "D":
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]


    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def go_up(self):
        """ Called when the user hits the up arrow. """
        self.change_y = -6
        self.direction = "U"

    def go_down(self):
        """ Called when the user hits the down arrow. """
        self.change_y = 6
        self.direction = "D"

    def stop_x(self, pressed_keys):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        if pressed_keys[K_UP]:
                self.direction = "U"
        if pressed_keys[K_DOWN]:
                self.direction = "D"

    def stop_y(self, pressed_keys):
        """ Called when the user lets off the keyboard. """
        self.change_y = 0
        if pressed_keys[K_LEFT]:
                self.direction = "L"
        if pressed_keys[K_RIGHT]:
                self.direction = "R"

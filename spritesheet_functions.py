"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame



class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
        self.file_name = file_name
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_sprite(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        sprite = pygame.Surface((width, height)).convert()
        sprite.set_colorkey((255, 0, 255))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite

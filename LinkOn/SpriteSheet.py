import pygame

class SpriteSheets(object):
    """ Class used to grab images out of a sprite sheet. """
    def __init__(self, file_name, color="white"):
        """ Constructor. Pass in the file name of the sprite sheet. """
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
        if color == "black":
            self.color = (0,0,0)
        elif color == "blue":
            self.color = (0,0,255)
        elif color == "white":
            self.color = (255,255,255)

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # Assuming black works as the transparent color
        image.set_colorkey(self.color)
        # Return the image
        return image

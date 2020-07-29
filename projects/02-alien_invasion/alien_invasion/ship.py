import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ A class to manage a ship """

    def __init__(self, ai_game): #reference to current instance of AlienInvasion
        """ Initialize the ship and set it's starting position. """
        super().__init__()
        self.screen = ai_game.screen # set screen attribute from the AlienInvasion, so we can easily access from here
        self.screen_rect =  ai_game.screen.get_rect() # allow us to place the ship in the correct location on the screen
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        # Load function returns us a Surface with the ball data.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # Match self.rect with center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        # Need to convert bacause X and Y takes by default only int
        self.x = float(self.rect.x)

        # Movement flag to False by default
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """ Update the ship position based on the movement flag """
        # Update the ship's X value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update self object from self.x
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship at it's current location """
        self.screen.blit(self.image, self.rect) # blit image onto the screen


    def center_ship(self):
        """ Center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
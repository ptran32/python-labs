import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class for Aliens """

    def __init__(self, game):
        super().__init__()

        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load('images/alien.bmp')
        
        # self.rect has to be name like this to avoid this below #
        #  self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        #   AttributeError: 'Alien' object has no attribute 'rect'
        self.rect = self.image.get_rect() 

        # Start each new alien near of the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exact horizontal position
        self.x = float(self.rect.x)


    def check_edges(self):
        """ Return True if an alien is in an edge of the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """ Move alien left or right """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
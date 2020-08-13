import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A Class to Represent a Single alien in a Fleet """
    def __init__(self, setting, screen):
        super(Alien, self).__init__()
        self.setting = setting
        self.screen = screen

        # Load alien image and set its Rect
        self.image = pygame.image.load('./images/alien_.png')
        self.rect = self.image.get_rect()

        # Start Each New Alien at top left of the Screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing exact Alien Position
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw alien at its Current Location """
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        """ Return True if alienis at edge of screen """
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Move the Alien to left or Right """
        self.x += (self.setting.alien_speed_factor * self.setting.fleet_direction)
        self.rect.x = self.x
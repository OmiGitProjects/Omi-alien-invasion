import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_setting, screen):
        """ Initialize the Ship and Starting Position """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #load the Ship Image
        self.ship_image = pygame.image.load('images/ship.png')
        self.rect = self.ship_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start Each new ship at the bottojm center of the screem
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        print(self.rect.centerx)
        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's Position based on the flag """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_setting.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        
        self.rect.centerx = self.center

    def blitme(self):
        """ Draw the ship at its current Location. """
        self.screen.blit(self.ship_image, self.rect)

    def center_ship(self):
        """ Center the Ship on the Screen """
        self.center = self.screen_rect.centerx
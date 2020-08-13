import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A Class to manage bullets fire from Ship """
    def __init__(self, setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a Bullet Rect (0, 0) and then set correct Position
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store a decimal Value
        self.y = float(self.rect.y)
        
        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        """ Move the bullet up the screen """
        # Update Decimal position of Bullet
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw Bullet to the Screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
import pygame.font

pygame.init()
class Button():
    """ Initialize Button Attribute """
    def __init__(self, setting, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        #Set the Dimension of the Button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Build rect's Object and Center it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Button Message needs to be Prepped Once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn Message into render image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        """ Draw Blank button then Message """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
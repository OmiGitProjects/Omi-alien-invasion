import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """ A Class to Report Scoring Information """
    def __init__(self, setting, screen, stats):
        """ Initialize Scorekeeping Attributes """
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.setting = setting
        self.stats = stats

        #Font Setting for Scoring INformation
        self.text_color = (255, 165, 0)
        self.font = pygame.font.Font('Rancho-Regular.ttf', 30)

        #Initial Prep Score
        self.prep_score()
        self.prep_high_score()
        self.prep_ship()
        self.prep_name()

    def prep_high_score(self):
        """ Turn the High Score into render image """
        high_score = int(round(self.stats.score, -1)) 
        high_score_str = "{:,}".format(high_score)
        self.highScore_image = self.font.render(high_score_str, True, self.text_color)

        #Display The highScore at Top of the Screen
        self.highScore_image_rect = self.highScore_image.get_rect()
        self.highScore_image_rect.centerx = self.screen_rect.centerx
        self.highScore_image_rect.top = 10
    
    def prep_name(self):
        """ Displaying Game Name With Owner Name """
        name = 'Omi Alien Invasion'
        self.name_image = self.font.render(name, True, self.text_color)

        #Display the Name at Top Left of the Screen
        self.name_image_rect = self.name_image.get_rect()
        self.name_image_rect.left = self.screen_rect.left + 10
        self.name_image_rect.top = 10

    def prep_score(self):
        """ Turn the Score to Render Image """
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        #Display the Score at Top-Right of the Screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 10
        self.score_rect.right = self.screen_rect.right - 10

    def prep_ship(self):
        """ How Many Ships Are Left """
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.setting, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """ Display the Scores """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highScore_image, self.highScore_image_rect)
        # self.ships.draw(self.screen)
        self.screen.blit(self.name_image, self.name_image_rect)
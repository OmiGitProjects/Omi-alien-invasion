""" Main Game Settings """

class Settings():
    """ A Class to Store all Settings of Alien Invasion """ 

    def __init__(self):
        # Initialize the Game's Settings
        self.screen_width = 800
        self.screen_height = 600    
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 4

        # Bullets Settings
        self.bullet_speed_factor = 10
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 3

        # Alien Setting
        self.alien_speed_factor = 3
        self.fleet_droped_speed = 30
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        #Game Stats
        self.ship_limit = 3

        #How Quickly the Game Speed Up
        self.speedup_scale = 1.1

        #How Quickly the Score Speed up
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 1.2
        
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """ Increase Speed Setting """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
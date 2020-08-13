import pygame as pg
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """ Initialize Game and Create a Screen Object """

    # Setting Object
    game_setting = Settings()
    screen = pg.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pg.display.set_caption("Alien Invasion")

    #Make Play Button
    playButton = Button(game_setting, screen, 'Play')


    #Create an Instance to store game statistics
    stats = Game_stats(game_setting)
    
    #Creating Instance of ScoreBoard
    sb = Scoreboard(game_setting, screen, stats)

    #Make a Ship
    ship = Ship(game_setting, screen)
    bullets = Group()
    aliens = Group()

    #Background
    bg = pg.image.load('./images/bg.png')

    # #Set Background color
    # bg_color = game_setting.bg_color
    gf.create_fleet(game_setting, screen, ship, aliens)

    while True:
        "Main Game Loop"

        # Keyboard and Mouse Events
        gf.check_events(game_setting, screen, stats, sb, ship, aliens, bullets, playButton)

        if stats.game_active:
            ship.update()
            gf.update_bullets(game_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_alien(game_setting, stats, screen, sb, ship, aliens, bullets)
            
        gf.update_screen(game_setting, screen, stats, sb, ship, aliens, bullets, bg, playButton)

if __name__ == '__main__':
    run_game()
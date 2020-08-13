import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
import sound_effect as se

def firing_bullet(settings, screen, ship, bullets):
    # Create a New Bullet and Add it to the bullet group
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
        se.bullet_sound.play()

def check_keydown_events(event, settings, screen, ship, bullets):
    """ Responds to keyPresses """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True    
    elif event.key == pygame.K_SPACE:
        firing_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """ Responds to keypress """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(setting, screen, stats, sb, ship, aliens, bullets, playButton, mouse_x, mouse_y):
    """ Start a New Game When Player Hits PLay """
    button_clicked = playButton.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Reset the Game Setting
        setting.initialize_dynamic_settings()

        #Reset the Game Statistics
        stats.reset_stats()
        stats.game_active = True

        #Reset the Scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_ship()

        #Hide the Mouse Cursor
        pygame.mouse.set_visible(False)

        #Remove All Aliens and Bullets
        aliens.empty()
        bullets.empty()

        #Create a New Fleet
        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_events(settings, screen, stats, sb, ship, aliens, bullets, playButton):
    """ Respond to Keypresses and Mouse Events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, ship, aliens, bullets, playButton, mouse_x, mouse_y)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
    

def update_screen(settings, screen, stats, sb, ship, alien, bullets, bg, playButton):
    """ Update images on the screen and flip to the new screen """

    # screen.fill(settings.bg_color)
    screen.blit(bg, (0,0))
    ship.blitme()
    alien.draw(screen)

    #Redraw All bullets Behind Ship and ALiens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Draw the Play Button if the game is Inactive
    if not stats.game_active:
        playButton.draw_button()

    sb.show_score()
    #Make the most recent drawn screen visible
    pygame.display.flip()

def update_bullets(setting, screen, stats, sb, ship, aliens, bullets):
    """ Update Bullets Position and Get Rid of Old Bullets"""
    bullets.update()

    #Get Rid of Old Bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    create_bullet_collision(setting, screen, stats, sb, ship, aliens, bullets)

def create_bullet_collision(setting, screen, stats, sb, ship, aliens, bullets):
    """ Bullet Collision Detection and Handling ALiens """
    # Check for any bullet that it hits aliens
    # if SO, than get rid of the Bullet and alien
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collision:
        se.alien_sound.play()
        for aliens in collision.values():
            stats.score += setting.alien_points
            sb.prep_score()
        check_high_score(stats, sb)
        
    #Check for Empty
    if len(aliens) == 0:
        # Destroy Existing Bullets, Speed up and create New Fleet
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting, screen, ship, aliens)

def get_number_alien_x(setting, alien_width):
    """ Determine the Number of Aliens fit in a row """
    avaliable_space_x = setting.screen_width - (2 * alien_width)
    number_alien_x = int(avaliable_space_x / (2 * alien_width))
    return number_alien_x

def get_number_row(setting, ship_height, alien_height):
    """ Get Number of Rows """
    avaliable_space_y = setting.screen_height - (3 * alien_height) - ship_height
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows

def create_fleet(setting, screen, ship, aliens):
    """ Create a Fleet of Aliens """
    # Create an Alien and find number of alien in a row
    # Spacing between each alien is equal to alien width
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    number_alien_x = get_number_alien_x(setting, alien_width)
    number_rows = get_number_row(setting, ship.rect.height, alien.rect.height)
    # Creating First Row of alien
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            # Create an Alien and placed it in row
            create_aliens(setting, aliens, screen, alien_number, alien_width, row_number)

def create_aliens(setting, aliens, screen, alien_number, alien_width, row_number):
    """ Create an Alien and placed it in row """
    alien = Alien(setting, screen)
    # alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def update_alien(setting, stats, screen, sb, ship, aliens, bullets):
    """ Update the position of all Alien Fleet """
    check_fleet_edge(setting, aliens)
    aliens.update()

    #Look For Alien Ship Collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(setting, stats, screen, sb, ship, aliens, bullets)

    #Look alien hitting at bottom of the SCreen
    check_alien_bottom(setting, stats, screen, sb, ship, aliens, bullets)

def check_fleet_edge(setting, aliens):
    """ Respond Appropriatly if any aliens have reached an Edge """
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(setting, aliens)
            break

def change_fleet_direction(setting, aliens):
    """ Drop entire fleet and Change Direction """
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_droped_speed
    setting.fleet_direction *= -1

def ship_hit(setting, stats, screen, sb, ship, aliens, bullets):
    """ Handling the Logic after ALiens Hit Ship """
    if stats.ship_left > 0:
        #Decrement the Ship limit by 1
        stats.ship_left -= 1

        #Update Scoreboard
        sb.prep_ship()

        #Empty the list of aliens and Bullets
        aliens.empty()
        bullets.empty()

        #Create New Fleet and Center the Ship
        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()

        #Pause
        sleep(0.5)
    else:
        # Setting 
        stats.game_active = False

def check_alien_bottom(setting, stats, screen, sb, ship, aliens, bullets):
    """ Checking the Aien reached at bottom of the Game """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat the Same as Ship got hit by Alien
            ship_hit(setting, stats, screen, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """ Check to see, if there is a Highscore """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        print(stats.high_score)
        sb.prep_high_score()
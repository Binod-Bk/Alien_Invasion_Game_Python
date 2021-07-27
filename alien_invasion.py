

import pygame
from ship import Ship
from settings import Settings
import game_functions as gf
from alien import Alien
from pygame.sprite import Group

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion ")
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #set a color


    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
            gf.create_fleet(ai_settings,screen,ship,aliens)
            gf.check_events(ai_settings,screen,ship,bullets)
            ship.update(screen)
        # Redraw the screen during each pass through the loop.
        # Make the most recently drawn screen visible.
            gf.update_bullets(bullets)

            gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()





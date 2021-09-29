

import pygame
from ship import Ship
from settings import Settings
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion ")
    play_button = Button(ai_settings, screen, "Play Now")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #set a color


    # Start the main loop for the game.
    while True:


            gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)

            if stats.game_active:
                ship.update(screen)

                gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
                gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            gf.update_screen(ai_settings,stats,screen,ship,aliens,bullets,play_button)

run_game()





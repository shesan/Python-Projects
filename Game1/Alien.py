import pygame
import game_functions
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():

    # Initialize the screen
    pygame.init()
    setting_store = Settings()
    screen = pygame.display.set_mode(
        (setting_store.screen_w, setting_store.screen_h))
    pygame.display.set_caption(setting_store.name)
    background_color = (230, 230, 230)

    # create the ship object
    ship = Ship(setting_store, screen)

    # create the bullet object
    bullets = Group()

    # Main loop of the game
    while True:
        # Check player input
        game_functions.check_events(setting_store, screen, ship, bullets)

        # Updates position of ship
        ship.update()

        # Update values of bullets
        game_functions.update_bullets(bullets)

        # update screen with new values
        game_functions.update_screen(setting_store, screen, ship, bullets)


# Call main
if __name__ == "__main__":
    run_game()

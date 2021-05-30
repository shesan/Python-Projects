import sys
import pygame
from bullet import Bullet


# Check if key is pressed down
def check_keydown_events(event, setting_store, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting_store, screen, ship, bullets)


# Check if key is pressed up (not pressed down)
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


# Event check
def check_events(setting_store, screen, ship, bullets):
    for event in pygame.event.get():

        # Check if exit is called
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, setting_store, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


# Screen Update
def update_screen(setting_store, screen, ship, bullets):
    screen.fill(setting_store.background_color)

    # draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # draw ship
    ship.blitme()

    # refresh display
    pygame.display.flip()


# Bullet Update
def update_bullets(bullets):
    bullets.update()
    # print(len(bullets))

    # remove waste bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


# Bullet Fire
def fire_bullet(setting_store, screen, ship, bullets):
    # Fire bullets
    if len(bullets) < setting_store.bullets_allowed:
        new_bullet = Bullet(setting_store, screen, ship)
        bullets.add(new_bullet)

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, setting_store, screen, ship):
        # Create bullet object at ship's position
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a new bullet rect at 0, 0 and reposition to ship
        self.rect = pygame.Rect(
            0, 0, setting_store.bullet_width, setting_store.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullets Y-value
        self.y = float(self.rect.y)

        # Bullet variables
        self.color = setting_store.bullet_color
        self.speed = setting_store.bullet_speed
        self.number = False

    def update(self):
        # update bullet position
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

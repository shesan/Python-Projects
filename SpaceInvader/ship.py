import pygame


class Ship():
    def __init__(self, setting_store, screen):
        self.setting_store = setting_store
        self.screen = screen

        # Ship load
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set position to center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Ship center position
        self.center = float(self.rect.centerx)

        # Movement
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting_store.ship_speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= self.setting_store.ship_speed

        # update the center of the ships so we can keep track of
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

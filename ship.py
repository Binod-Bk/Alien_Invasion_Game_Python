
import pygame

class Ship:

    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.image = pygame.image.load('images/space3.bmp')
        self.image = pygame.transform.scale(self.image,(50,60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

    def update(self,screen):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)



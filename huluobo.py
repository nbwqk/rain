import pygame
from pygame.sprite import Sprite
import random

class Huluobo(Sprite):
    def __init__(self,r_settings,screen):
        super(Huluobo,self).__init__()
        self.screen=screen
        self.r_settings=r_settings

        self.image=pygame.image.load('images/huluobo.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=random.randrange(0,r_settings.screen_width)
        self.rect.bottom=0

        self.centery=float(self.rect.centery)

    def update(self):
        self.centery += self.r_settings.huluobo_speed_factor
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image,self.rect)



import pygame
from pygame.sprite import Sprite

class Man(Sprite):
    def __init__(self,r_settings,screen):
        super(Man, self).__init__()
        # 初始化飞船并设置其初始位置
        self.screen=screen
        self.r_settings=r_settings

        # 加载小人图像并获取其外形矩形
        self.image=pygame.image.load('images/man.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # 将每个小人放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        # 在小人的属性center中存储小数值
        self.center=float(self.rect.centerx)
        # 移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标志调整小人的位置"""
        # 更新小人的center值，而不是rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.r_settings.man_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.r_settings.man_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx=self.center

    def center_man(self):
        self.rect.centerx=self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image,self.rect)

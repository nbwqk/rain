import pygame,sys
import game_function as gf
from man import Man
from huluobo import Huluobo
from settings import Settings
from pygame.sprite import Group

def run_game():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    r_settings=Settings()
    screen=pygame.display.set_mode((r_settings.screen_width,r_settings.screen_height))
    pygame.display.set_caption('rain')

    man=Man(r_settings,screen)
    huluobos=Group()

    while True:
        gf.check_event(man)
        man.update()
        gf.update_huluobos(r_settings,screen,huluobos)
        gf.update_screen(r_settings,screen,man,huluobos)

run_game()
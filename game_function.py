import pygame,sys
from huluobo import Huluobo

def check_down_events(event,man):
    if event.key == pygame.K_RIGHT:
        man.moving_right = True
    elif event.key == pygame.K_LEFT:
        man.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_up_event(event,man):
    if event.key == pygame.K_RIGHT:
        man.moving_right = False
    if event.key == pygame.K_LEFT:
        man.moving_left = False

def check_event(man):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_events(event,man)
        elif event.type == pygame.KEYUP:
            check_up_event(event,man)

def huluobo_diaoluo(r_settings,screen,huluobos):
    new_huluobo=Huluobo(r_settings,screen)
    huluobos.add(new_huluobo)

def update_huluobos(r_settings,screen,huluobos,man):
    if len(huluobos) <= 2:
       huluobo_diaoluo(r_settings,screen,huluobos)
    huluobos.update()
    for huluobo in huluobos.copy():
        if huluobo.rect.y > 800 or pygame.sprite.spritecollideany(man,huluobos):
            huluobos.remove(huluobo)


def update_screen(r_settings,screen,man,huluobos):
    screen.fill(r_settings.bg_color)
    man.blitme()
    for huluobo in huluobos.sprites():
        huluobo.blitme()
    pygame.display.flip()

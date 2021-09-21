import pygame
import sys
from pygame.locals import *
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{1000},{200}'

pygame.init()

canvas = pygame.display.set_mode((480, 640))
pygame.display.set_caption('space invaders')
clock = pygame.time.Clock()

ship = pygame.image.load('spaceship.png')
bullet = pygame.image.load('bullet.png')
a = False
d = False
x = canvas.get_width() / 2 - ship.get_width() / 2
y = canvas.get_height() - ship.get_height()
fire = False
bullet_x = x
bullet_y = y
bullet_visible = False

# 사용자 입력
# 연산
# 그리기
# 애니메이션 연산

while True:
    # 입력
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == ord("a"):
                a = True
            if event.key == ord("d"):
                d = True
            if event.key == pygame.K_SPACE:
                if bullet_visible == False:
                    fire = True

        if event.type == KEYUP:
            if event.key == ord("a"):
                a = False
            if event.key == ord("d"):
                d = False
        

    # 연산
    if a == True:
        x -= 5
    if d == True:
        x += 5
    if x >= canvas.get_width() - ship.get_width():
        x = canvas.get_width() - ship.get_width()
    if x < 0:
        x = 0
    if fire:
        bullet_visible = True
        bullet_x = x + ship.get_width() / 2 - bullet.get_width() / 2 + 1
        bullet_y = y 
        fire = False
    bullet_y -= 5    
    if bullet_y < 0:
        bullet_visible = False



    # 그리기
    canvas.fill((255,255,255))
    canvas.blit(ship,(x, y))
    if bullet_visible:
        canvas.blit(bullet, (bullet_x, bullet_y))    


    pygame.display.update()

    clock.tick(60)

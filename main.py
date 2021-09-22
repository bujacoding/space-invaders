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
shoot = pygame.mixer.Sound('res/sound/shoot.wav')
enemy = pygame.image.load('res/sprite/enemy.png')
a = False
d = False
x = canvas.get_width() / 2 - ship.get_width() / 2
y = canvas.get_height() - ship.get_height()
fire = False
bullet_x = x
bullet_y = y
bullet_visible = False
enemy_x = 0
enemy_y = 0
left_to_right = True
enemy_visible = True
b_collision = False

#상수
BULLET_SPEED = 15
SHIP_SPEED = 5

# 사용자 입력
# 연산
# 그리기
# 애니메이션 연산

def collision(a_x1, a_x2, a_y1, a_y2, b_x1, b_x2, b_y1, b_y2):
    t = False
    if a_x2 < b_x1: #bullet = a , enemy = b
        t = False
    elif b_x2 < a_x1:
        t = False
    elif b_y2 < a_y1:
        t = False
    elif a_y2 < b_y1:
        t = False
    else:
        t = True

    if t == True:
        print(b_collision)
    return t

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
                    shoot.play()

        if event.type == KEYUP:
            if event.key == ord("a"):
                a = False
            if event.key == ord("d"):
                d = False
        

    # 연산
    if a == True:
        x -= SHIP_SPEED
    if d == True:
        x += SHIP_SPEED
    if x >= canvas.get_width() - ship.get_width():
        x = canvas.get_width() - ship.get_width()
    if x < 0:
        x = 0
    if fire:
        bullet_visible = True
        bullet_x = x + ship.get_width() / 2 - bullet.get_width() / 2 + 1
        bullet_y = y 
        fire = False

    bullet_y -= BULLET_SPEED    
    if bullet_y < 0:
        bullet_visible = False

    e_x2 = enemy_x + enemy.get_width()
    e_y2 = enemy_y + enemy.get_height()
    b_x2 = bullet_x + bullet.get_width()
    b_y2 = bullet_y + bullet.get_height()

    # if b_x2 < enemy_x:
    #     collision = False
    # elif e_x2 < bullet_x:
    #     collision = False
    # elif e_y2 < bullet_y:
    #     collision = False
    # elif  b_y2 < enemy_y:
    #     collision = False
    # else:
    #     collision = True
    
    b_collision = collision(enemy_x, e_x2, enemy_y, e_y2, bullet_x, b_x2, bullet_y, b_y2)

    if b_collision == True:
        bullet_visible = False
        fire = False
        enemy_visible = False

    if enemy_visible == False:
        left_to_right = True
        enemy_x = 0
        enemy_y = 0
        enemy_visible = True
        



    if left_to_right:
        if enemy_visible:
            enemy_x += 3
            if canvas.get_width() < enemy_x + enemy.get_width():
                enemy_y += enemy.get_height()
                left_to_right = False


    else:
        if enemy_visible:
            enemy_x -= 3
            if enemy_x < 0:
                enemy_y += enemy.get_height()
                left_to_right = True
            

    # 그리기
    canvas.fill((255,255,255))
    canvas.blit(ship,(x, y))
    if bullet_visible:
        canvas.blit(bullet, (bullet_x, bullet_y))    
    if enemy_visible:
            canvas.blit(enemy, (enemy_x,enemy_y))

    pygame.display.update()

    clock.tick(60)

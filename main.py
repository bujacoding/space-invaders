from manager import Manager
import pygame
import sys
from pygame.locals import *
import os
from enemy import Enemy
from ship import Ship

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{1000},{200}'

pygame.init()

pause = False
canvas = pygame.display.set_mode((480, 640))
pygame.display.set_caption('space invaders')
clock = pygame.time.Clock()

bullet = pygame.image.load('res/sprite/bullet.png')
shoot = pygame.mixer.Sound('res/sound/shoot.wav')

manager = Manager()
ship = Ship()
enemies = [Enemy(manager), Enemy(manager), Enemy(manager),
           Enemy(manager), Enemy(manager), ]
for index, enemy in enumerate(enemies):
    enemy.set_x(index * enemy.get_width())

ship.set_initial_position(canvas)
fire = False
bullet_x = 0
bullet_y = 0
bullet_visible = False
b_collision = False


# 상수
BULLET_SPEED = 15

# 사용자 입력
# 연산
# 그리기
# 애니메이션 연산


def collision(a_x1, a_x2, a_y1, a_y2, b_x1, b_x2, b_y1, b_y2):
    if a_x2 < b_x1:
        return False
    elif b_x2 < a_x1:
        return False
    elif b_y2 < a_y1:
        return False
    elif a_y2 < b_y1:
        return False
    else:
        return True


while True:
    # 입력
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == ord("p"):
                pause = not pause

        if not pause and event.type == KEYDOWN:
            if event.key == ord("a"):
                ship.move_to_left = True
            if event.key == ord("d"):
                ship.move_to_right = True
            if event.key == pygame.K_SPACE:
                if bullet_visible == False:
                    fire = True
                    shoot.play()

        if not pause and event.type == KEYUP:
            if event.key == ord("a"):
                ship.move_to_left = False
            if event.key == ord("d"):
                ship.move_to_right = False

    # 연산
    if not pause:
        ship.update(canvas)
        if fire:
            bullet_visible = True
            bullet_x = ship.x + ship.sprite.get_width() / 2 - bullet.get_width() / 2 + 1
            bullet_y = ship.y
            fire = False

        bullet_y -= BULLET_SPEED
        if bullet_y < 0:
            bullet_visible = False
        manager.update()

        for enemy in enemies:
            enemy.update(canvas)

        manager.clear()

    # 그리기
    canvas.fill((255, 255, 255))
    if bullet_visible:
        canvas.blit(bullet, (bullet_x, bullet_y))

    for enemy in enemies:
        enemy.render(canvas)
    ship.render(canvas)

    pygame.display.update()

    clock.tick(60)

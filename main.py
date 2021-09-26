from enemy_manager import EnemyManager
import pygame
import sys
from pygame.locals import *
import os
from enemy import Enemy
from ship import Ship
from object_manager import ObjectManager

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{1000},{200}'

pygame.init()

pause = False
canvas = pygame.display.set_mode((480, 640))
pygame.display.set_caption('space invaders')
clock = pygame.time.Clock()

object_manager = ObjectManager()

shoot = pygame.mixer.Sound('res/sound/shoot.wav')

enemy_manager = EnemyManager()
ship = Ship()
object_manager.append(ship)

enemies = [Enemy(enemy_manager), Enemy(enemy_manager), Enemy(enemy_manager),
           Enemy(enemy_manager), Enemy(enemy_manager), ]

for index, enemy in enumerate(enemies):
    enemy.set_x(index * enemy.get_width())
    object_manager.append(enemy)

ship.set_initial_position(canvas)

b_collision = False


# 상수


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
                ship.move_to_left = False
                ship.move_to_right = False
                pause = not pause

        if not pause and event.type == KEYDOWN:
            if event.key == ord("a"):
                ship.move_to_left = True
            if event.key == ord("d"):
                ship.move_to_right = True
            if event.key == pygame.K_SPACE:
                ship.fire(object_manager)

        if not pause and event.type == KEYUP:
            if event.key == ord("a"):
                ship.move_to_left = False
            if event.key == ord("d"):
                ship.move_to_right = False

    # 연산
    if not pause:
        enemy_manager.update()
        object_manager.update(canvas)
        enemy_manager.clear()

    # 그리기
    canvas.fill((255, 255, 255))

    object_manager.render(canvas)

    pygame.display.update()

    clock.tick(60)

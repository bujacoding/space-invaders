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

# enemy 공통
left_to_right = True

# enemy 개별
enemy = pygame.image.load('res/sprite/enemy.png')
# enemy_x = 0
# enemy_y = 0
# enemy_visible = True

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('res/sprite/enemy.png')
        self.x = 0
        self.y = 0

    def set_x(self, x):
        self.x = x


    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def update(self):
        global left_to_right
        if left_to_right:
            self.x += 3
            if canvas.get_width() < self.x + self.get_width():
                self.y += self.get_height()
                left_to_right = False


        else:
            self.x -= 3
            if self.x < 0:
                self.y += self.get_height()
                left_to_right = True
            

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))


enemies = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy(),]
for index, enemy in enumerate(enemies):
    enemy.set_x(index * enemy.get_width())

a = False
d = False
x = canvas.get_width() / 2 - ship.get_width() / 2
y = canvas.get_height() - ship.get_height()
fire = False
bullet_x = x
bullet_y = y
bullet_visible = False
b_collision = False

#상수
BULLET_SPEED = 15
SHIP_SPEED = 5

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

    for enemy in enemies:
        enemy.update()

    # 그리기
    canvas.fill((255,255,255))
    canvas.blit(ship,(x, y))
    if bullet_visible:
        canvas.blit(bullet, (bullet_x, bullet_y))
    
    for enemy in enemies:
        enemy.render(canvas)

    pygame.display.update()

    clock.tick(60)

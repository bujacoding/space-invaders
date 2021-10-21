import pygame
from pygame.locals import *
BULLET_SPEED = 15


class Bullet():
    bulletcount = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load('res/sprite/bullet.png')
        self.sound = pygame.mixer.Sound("res/sound/shoot.wav")
        self.sound.play()

    def render(self, canvas):
        canvas.blit(self.sprite, (self.x, self.y))

    def update(self, canvas):
        self.y -= BULLET_SPEED
        for enemy in self.enemies:
            if self.collision(enemy):
                self.object_manager.kill(self)
                self.object_manager.kill(enemy)
                self.enemies.remove(enemy)
        if self.y <= 0:
            self.object_manager.kill(self)

        # enemy 하나씩 충돌 여부 확인
        # 충돌하였으면, 폭파시키고, 총알과 적기 사라짐

    def collision(self, enemy) -> bool:
        a_x2 = self.x + self.sprite.get_width()
        a_y2 = self.y + self.sprite.get_height()
        b_x2 = enemy.x + enemy.get_width()
        b_y2 = enemy.y + enemy.get_height()

        if a_x2 < enemy.x:
            return False
        elif b_x2 < self.x:
            return False
        elif b_y2 < self.y:
            return False
        elif a_y2 < enemy.y:
            return False
        else:
            return True

    def onKilled(self):
        Bullet.bulletcount -= 1

import pygame
from pygame.locals import *
BULLET_SPEED = 15


class Bullet():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = pygame.image.load('res/sprite/bullet.png')
        self.visible = True
        self.fire

    def render(self, canvas):
        if self.visible:
            canvas.blit(self.sprite, (self.x, self.y))

    def update(self):
        self.y -= BULLET_SPEED
        if self.y < 0:
            self.visible = False

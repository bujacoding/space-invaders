import pygame
from pygame.locals import *
BULLET_SPEED = 15


class Bullet():
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

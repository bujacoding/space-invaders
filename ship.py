import pygame
from pygame.locals import *
SHIP_SPEED = 5


class Ship():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = pygame.image.load('res/sprite/spaceship.png')
        self.a = False
        self.d = False

    def render(self, canvas):
        canvas.blit(self.sprite, (self.x, self.y))

    def set_initial_position(self, canvas):
        self.x = canvas.get_width() / 2 - self.sprite.get_width() / 2
        self.y = canvas.get_height() - self.sprite.get_height()

    def update(self, canvas):
        if self.a == True:
            self.x -= SHIP_SPEED
        if self.d == True:
            self.x += SHIP_SPEED
        if self.x >= canvas.get_width() - self.sprite.get_width():
            self.x = canvas.get_width() - self.sprite.get_width()
        if self.x < 0:
            self.x = 0

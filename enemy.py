import pygame
import sys
from pygame.locals import *

# enemy 공통
left_to_right = True

enemy = pygame.image.load('res/sprite/enemy.png')


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

    def update(self, canvas):
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

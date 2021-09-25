import pygame
from pygame.locals import *


class Ship():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = pygame.image.load('res/sprite/spaceship.png')

    def render(self, canvas):
        canvas.blit(self.sprite, (self.x, self.y))

    def set_initial_position(self, canvas):
        self.x = canvas.get_width() / 2 - self.sprite.get_width() / 2
        self.y = canvas.get_height() - self.sprite.get_height()

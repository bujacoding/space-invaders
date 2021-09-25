import pygame
import sys
from pygame.locals import *


class Enemy:
    def __init__(self, manager):
        self.image = pygame.image.load('res/sprite/enemy.png')
        self.x = 0
        self.y = 0
        self.manager = manager

    def set_x(self, x):
        self.x = x

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def is_reached(self, canvas) -> bool:
        if self.manager.left_to_right:
            return canvas.get_width() < self.x + self.get_width()
        else:
            return self.x < 0

    def update(self, canvas):

        # 끝에 닿았는가? -> 함수로 만들어 보자
        if self.is_reached(canvas):
            # 매니저에게 알리기
            self.manager.change_direction()

        # 정해진 방향으로 이동
        if self.manager.left_to_right:
            self.x += 3
        else:
            self.x -= 3

    def move_down(self):
        self.y += self.get_height()

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))

import pygame
import sys
from pygame.locals import *

# enemy 공통
left_to_right = True


class Enemy:
    def __init__(self):
        self.image = pygame.image.load('res/sprite/enemy.png')
        self.x = 0
        self.y = 0
        self.last_direction = left_to_right

    def set_x(self, x):
        self.x = x

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def is_reached(self, canvas) -> bool:
        global left_to_right
        if left_to_right:
            return canvas.get_width() < self.x + self.get_width()
        else:
            return self.x < 0

    def need_to_go_down(self):
        return self.last_direction != left_to_right

    def update(self, canvas):

        global left_to_right

        # 끝에 닿았는가? -> 함수로 만들어 보자
        if self.is_reached(canvas):
            # 모두에게 알리기
            left_to_right = not left_to_right

        # 정해진 방향으로 이동
        if left_to_right:
            self.x += 3
        else:
            self.x -= 3

        # 내려가야 하는가?
        if self.need_to_go_down():
            self.y += self.get_height()
            self.last_direction = left_to_right

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))

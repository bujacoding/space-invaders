import pygame
import sys
from pygame.locals import *

pygame.init()

displaysurf = pygame.display.set_mode((480, 640))
pygame.display.set_caption('space invaders')
clock = pygame.time.Clock()

ship = pygame.image.load('spaceship.png')
a = False
d = False
x = 0
y = 0

while True:
    displaysurf.fill((255,255,255))
    displaysurf.blit(ship,(x, y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == ord("a"):
                a = True
            if event.key == ord("d"):
                d = True
        if event.type == KEYUP:
            if event.key == ord("a"):
                a = False
            if event.key == ord("d"):
                d = False
    if a == True:
        x -= 5
    if d == True:
        x += 5

    clock.tick(60)
    pygame.display.update()
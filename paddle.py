import pygame
from object import object
class Paddle(object):
    def __init__(self, x, y, width, height, color, player):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 3
        self.player = player

    def update (self) :
        ## Funktion som styr paddlen
        if self.player == 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed
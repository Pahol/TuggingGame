import pygame
from pygame.locals import *

#########################################
moveDistance = 30

leftPlayer = pygame.image.load('picture/leftPlayer.png')

class LeftPlayer(object):

    def __init__(self, pos, height = 100, width = 100):
        self.pos = pos
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(leftPlayer, (int(self.height), int(self.width)))

    def can_hit(self, ball):
        return self.pos-self.width/2.0 < ball.y < self.pos+self.width/2.0 \
            and ball.x-ball.radius < self.THICKNESS

    def move_left(self):
        self.pos = (self.pos[0]-moveDistance, self.pos[1])

    def move_right(self):
        self.pos = (self.pos[0]+moveDistance, self.pos[1])

    def render(self, surface):
        surface.blit(self.image, self.pos)


#############################################


rightPlayer = pygame.image.load('picture/rightPlayer.png')

class RightPlayer(object):

    def __init__(self, pos, height = 100, width = 100):
        self.pos = pos
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(rightPlayer, (int(self.height), int(self.width)))

    def can_hit(self, ball):
        return self.pos-self.width/2.0 < ball.y < self.pos+self.width/2.0 \
            and ball.x-ball.radius < self.THICKNESS

    def move_left(self):
        self.pos = (self.pos[0]-moveDistance, self.pos[1])

    def move_right(self):
        self.pos = (self.pos[0]+moveDistance, self.pos[1])

    def render(self, surface):
        surface.blit(self.image, self.pos)
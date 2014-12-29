import pygame
from pygame.locals import *

import gamelib
from elements import LeftPlayer, RightPlayer

class TuggingGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    
    def __init__(self):
        super(TuggingGame, self).__init__('TuggingGame', TuggingGame.BLACK)
        self.leftplayer = LeftPlayer(pos = (350, 500))
        self.rightplayer = RightPlayer(pos = (800, 500))
        self.score = 0

    def init(self):
        super(TuggingGame, self).init()

    def update(self):
        pass

    def on_key_up(self, key):
        if key == K_d:
            self.leftplayer.move_left()
            self.rightplayer.move_left()
        elif key == K_l:
            self.leftplayer.move_right()
            self.rightplayer.move_right()

    def render(self, surface):
        self.leftplayer.render(surface)
        self.rightplayer.render(surface)

def main():
    game = TuggingGame()
    game.run()

if __name__ == '__main__':
    main()
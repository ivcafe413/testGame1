import sys
import logging

import pygame

from game import Game

TARGET_FPS = 60

class Runner:
    def __init__(self):
        pygame.init()

        self.game = Game.Game()

        # Render
        self.screen = pygame.display.set_mode((800, 600))

        self.gameClock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def run(self):
        while True:
            self.handle_events()

            fps = self.gameClock.get_fps()
            pygame.display.set_caption("FPS: {0:2f}".format(fps))
            self.gameClock.tick(TARGET_FPS)

def main():
    logging.basicConfig(level=logging.INFO)
    Runner().run()
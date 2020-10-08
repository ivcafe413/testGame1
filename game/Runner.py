import sys
import logging

from collections import defaultdict

import pygame

from game.Game import Game
from game.Renderer import Renderer

TARGET_FPS = 60
LOOP_MS_PF = (1 / TARGET_FPS) * 1000

class Runner:
    def __init__(self):
        pygame.init()

        self.gameState = Game()

        # Render
        rendererOptions = type('', (), {})()
        rendererOptions.game = self.gameState
        rendererOptions.width = 800
        rendererOptions.height = 600
        self.gameRenderer = Renderer(rendererOptions)

        self.gameClock = pygame.time.Clock()
        self.currentTime = 0

        # Event Handler dicts
        self.keydownHandlers = defaultdict(list)
        self.keyupHandlers = defaultdict(list)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydownHandlers[event.key]:
                    handler(event.type)
            elif event.type == pygame.KEYUP:
                for handler in self.keyupHandlers[event.key]:
                    handler(event.type)

    def run(self):
        # Initial Key Bindings
        self.keydownHandlers[pygame.K_LEFT].append(self.gameState.action_left)
        self.keydownHandlers[pygame.K_RIGHT].append(self.gameState.action_right)
        self.keydownHandlers[pygame.K_UP].append(self.gameState.action_up)
        self.keydownHandlers[pygame.K_DOWN].append(self.gameState.action_down)

        self.keyupHandlers[pygame.K_LEFT].append(self.gameState.action_left)
        self.keyupHandlers[pygame.K_RIGHT].append(self.gameState.action_right)
        self.keyupHandlers[pygame.K_UP].append(self.gameState.action_up)
        self.keyupHandlers[pygame.K_DOWN].append(self.gameState.action_down)

        # Game Loop Start
        while True: # TODO: Eventually implement frame pausing
            self.currentTime += self.gameClock.get_time()
            self.handle_events()

            while self.currentTime >= LOOP_MS_PF:
                self.gameState.update() # Passing in update MS diff?
                self.currentTime -= LOOP_MS_PF

            self.gameRenderer.render() # TODO: Passing in leftover ticks for delta rendering?

            fps = self.gameClock.get_fps()
            pygame.display.set_caption("FPS: {0:2f}".format(fps))
            self.gameClock.tick(TARGET_FPS)

def main():
    logging.basicConfig(level=logging.INFO)
    Runner().run()
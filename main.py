import pygame, sys
from sys import *

class Game:
    def __init__(self): 
        pygame.init()
        pygame.display.set_caption("Rancher's Hope")
        
        self.screen = pygame.display.set_mode((1430,700))
        self.clock = pygame.time.Clock()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
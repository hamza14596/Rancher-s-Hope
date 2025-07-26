import pygame
from settings import *

def __init__ (self):
    self.display_surface = pygame.display.get_surface()

    self.all_sprites = pygame.sprite.group()
    

def run(self,dt):
    self.all_sprites.draw (self.display_surface)
    self.display_surface.fill('black')
    self.all_sprites.update()
    
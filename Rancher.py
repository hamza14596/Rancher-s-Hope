import pygame
from settings import * 
class  Player(pygame.sprite.Sprite):
     def  __init__(self,position,group):
          super().__init__(group)
          self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
          self.image.fill('green')
          self.rect = self.image.get_rect(center = position)
    

        

    
import pygame
from settings import * 

class general (pygame.sprite.Sprite):
        def __init__(self,position, surf, groups, z = LAYERS['main'] ):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_rect(topleft=position)
            self.z = z

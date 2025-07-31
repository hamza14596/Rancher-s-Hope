import pygame
from settings import * 

class general (pygame.sprite.Sprite):
        def __init__(self,position, surf, groups, z = LAYERS['main'] ):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_rect(topleft=position)
            self.z = z

class Water(general):
    def __init__(self, position, frames, groups):
         #Animating the water set up 
            self.frames = frames
            self.frame_index = 0 

            super().__init__(
                position = position,   
                surf = self.frames[self.frame_index], 
                groups = groups,
                z = LAYERS['water'])  
                        

    def animate(self,dt):        
                self.frame_index += 7 * dt
                if self.frame_index >= len(self.frames):
                        self.frame_index = 0
                self.image = self.frames[int(self.frame_index)]
    def update(self,dt):
        self.animate(dt)   
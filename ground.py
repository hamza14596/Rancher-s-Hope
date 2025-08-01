import pygame
from settings import * 
from random import randint

class general (pygame.sprite.Sprite):
        def __init__(self,position, surf, groups, z = LAYERS['main'] ):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_rect(topleft=position)
            self.z = z
            self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

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


class wildflower(general):
       def __init__ (self,position,surf,groups):
              super().__init__(position,surf,groups)  
              self.hitbox = self.rect.copy().inflate(-20,-self.rect.height * 0.9)      
class tree(general):
       def __init__(self,position,surf,groups,name):
              super().__init__(position,surf,groups)


              #apples
              self.apple_surface = pygame.image.load('../graphics/fruit/apple.png')
              self.apple_position = APPLE_POS[name]
              self.apple_sprites = pygame.sprite.Group()
              self.create_fruit()

       def create_fruit(self):
              for position  in self.apple_position:
                     if randint(0,10) < 2:
                            x = position[0] + self.rect.left
                            y = position[1] + self.rect.top
                            general(
                                   position = (x,y),
                                   surf = self.apple_surface,
                                   groups = [self.apple_sprites,self.groups()[0]],
                                   z = LAYERS['fruit'])
                            
                     

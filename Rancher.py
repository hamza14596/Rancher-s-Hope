import pygame
from settings import * 
from help import *

class  Player(pygame.sprite.Sprite):
     def  __init__(self,position,group):
          super().__init__(group)
          
          self.import_assests()
          self.status = 'down'  
          self.frame_index = 0



          self.image = self.animations[self.status][self.frame_index]
          self.rect = self.image.get_rect(center = position)

          self.direction = pygame.math.Vector2()
          self.position = pygame.math.Vector2(self.rect.center)   
          self.speed = 200
     def import_assests(self):
          self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                            'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
                            'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],}
             
          for animation in self.animations.keys():
                full_path = '../graphics/character/' + animation + '/'
                self.animations[animation] = import_folder(full_path)
          print(self.animations)
     def animate(self,dt):
          self.frame_index += 6 * dt
          if self.frame_index >= len(self.animations[self.status]):
                 self.frame_index = 0

          self.image= self.animations[self.status][int(self.frame_index)]


     def input(self):
          keys = pygame.key.get_pressed()
          if keys[pygame.K_UP]:
              self.direction.y= -1
          elif keys[pygame.K_DOWN]:
              self.direction.y = 1
          else:
                self.direction.y = 0


          if keys[pygame.K_LEFT]:
              self.direction.x= -1
          elif keys[pygame.K_RIGHT]:
              self.direction.x = 1
          else:
                    self.direction.x = 0    
          
     def move(self,dt):
          if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()


          self.position.x += self.direction.x * self.speed * dt
          self.rect.centerx = self.position.x

          self.position.y += self.direction.y * self.speed * dt
          self.rect.centery = self.position.y
          
          

     def update(self,dt):
          self.input()
          self.move(dt)
          self.animate(dt)

    
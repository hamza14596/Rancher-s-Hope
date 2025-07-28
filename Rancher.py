import pygame
from settings import * 
from help import *
from ticker import Ticker

class  Player(pygame.sprite.Sprite):
     def  __init__(self,position,group):
          super().__init__(group)
          
          self.import_assests()
          self.status = 'down'  
          self.frame_index = 0


          #Player Spriten Setup
          self.image = self.animations[self.status][self.frame_index]
          self.rect = self.image.get_rect(center = position)

          #Player Movement Setup
          self.direction = pygame.math.Vector2()
          self.position = pygame.math.Vector2(self.rect.center)   
          self.speed = 200

          #Timer
          self.timers = {
               'tool use' : Ticker (350,self.use_tool),
               'tool switch':Ticker (200)
          }

          #tools 
          self.tools = ['water', 'hoe', 'axe']
          self.tool_index= 0
          self.selected_tool = self.tools[self.tool_index]


     #Tool Use
     def use_tool(self):
          keys = pygame.key.get_pressed()
          if keys [pygame.K_SPACE]:
               self.timers['tool use'].activate()
               print('using tool')
      



     def import_assests(self):
          self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                            'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
                            'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
                            'right_water': [], 'left_water': [], 'up_water': [], 'down_water': [],}
             
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
          if not self.timers['tool use'].active:
               keys = pygame.key.get_pressed()
               if keys[pygame.K_w]:
                    self.direction.y= -1
                    self.status = 'up'
               elif keys[pygame.K_s]:
                    self.direction.y = 1
                    self.status= 'down'
               else:
                    self.direction.y = 0


               if keys[pygame.K_a]:
                    self.direction.x= -1
                    self.status = 'left'
               elif keys[pygame.K_d]:
                    self.direction.x = 1
                    self.status = 'right'
               else:
                         self.direction.x = 0    
               #Tool Use
               if  keys[pygame.K_SPACE]:
                    self.timers['tool use'].activate()
                    self.direction = pygame.math.Vector2()
                    self.frame_index = 0

               #Change Tool
               # change tool
               if keys[pygame.K_q] and not self.timers['tool switch'].active:
                    self.timers['tool switch'].activate()
                    self.tool_index += 1

               if self.tool_index < len(self.tools):
                    self.tool_index = self.tool_index
               else:
                    self.tool_index = 0

               print(self.tool_index)
               self.selected_tool = self.tools[self.tool_index]

                    




     def get_status(self):     #used to add _idle to the status when not moving
         if self.direction.magnitude() == 0:
              self.status = self.status.split('_')[0] + '_idle'


         if self.timers['tool use'].active: 
              self.status = self.status.split('_')[0] + '_' + self.selected_tool


     #Update Timers
     def update_ticker(self):
          for timers in self.timers.values():
               timers.update() 


     def move(self,dt):     
          if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()


          self.position.x += self.direction.x * self.speed * dt
          self.rect.centerx = self.position.x

          self.position.y += self.direction.y * self.speed * dt
          self.rect.centery = self.position.y
          
          

     def update(self,dt):
          self.input()
          self.get_status()
          self.move(dt)
          self.animate(dt)
          self.update_ticker()
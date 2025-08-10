import pygame
from settings import *
from Rancher import Player
from overlay import Overlay
from ground import general, Water, wildflower, tree, interaction
from pytmx.util_pygame import load_pygame
from help import *
from transition import transition
from soil import SoilLayer


class Level:
    def __init__ (self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.collision_sprites = pygame.sprite.Group()
        self.tree_sprites = pygame.sprite.Group()

        self.tree_sprites = pygame.sprite.Group()
        self.apple_sprites = pygame.sprite.Group()
        self.interaction_sprites =pygame.sprite.Group()
        self.soil_layer = SoilLayer(self.all_sprites)
        self.setup()
        self.overlay = Overlay(self.player)
        self.transition = transition(self.reset, self.player)
       

    def setup(self):
        tmx_data = load_pygame('../data/map.tmx')
        
        
        #house 
        for layer in['HouseFloor','HouseFurnitureBottom']:
            for x,y, surf in tmx_data.get_layer_by_name(layer).tiles():
                    general((x * TILE_SIZE,y * TILE_SIZE),surf,self.all_sprites,LAYERS['house bottom'])

        
        for layer in['HouseWalls','HouseFurnitureTop']:
            for x,y, surf in tmx_data.get_layer_by_name(layer).tiles():
                    general((x * TILE_SIZE,y * TILE_SIZE),surf,self.all_sprites,LAYERS['main'])


         #fence
        for x,y, surf in tmx_data.get_layer_by_name('Fence').tiles():
                     general((x * TILE_SIZE,y * TILE_SIZE),surf,[self.all_sprites, self.collision_sprites], LAYERS['main'])

        #Water
        water_frames=import_folder('../graphics/water')
        for x,y, surf in tmx_data.get_layer_by_name('Water').tiles():
            Water((x * TILE_SIZE,y * TILE_SIZE),water_frames, self.all_sprites)

        #Trees     
        for obj in tmx_data.get_layer_by_name('Trees'):
             tree(
                  position=(obj.x,obj.y),
                  surf=obj.image,
                  groups=[self.all_sprites,self.collision_sprites,self.tree_sprites],
                  name=obj.name,
                  player_add = self.player_add
                      )     
          
        #Wildflower
        for obj in tmx_data.get_layer_by_name('Decoration'):
             wildflower((obj.x,obj.y),obj.image, [self.all_sprites,self.collision_sprites] )

        #collision tiles
        for x,y, surf in tmx_data.get_layer_by_name('Collision').tiles():
             general((x * TILE_SIZE,y * TILE_SIZE),pygame.Surface((TILE_SIZE,TILE_SIZE)),self.collision_sprites)
             
        #Player
        for obj in tmx_data.get_layer_by_name('Player'):
             if obj.name == 'Start':
                self.player = Player(
                    position=(obj.x,obj.y),
                    group=self.all_sprites,
                    collision_sprites=self.collision_sprites,
                    tree_sprites = self.tree_sprites,
                    interaction = self.interaction_sprites,
                    soil_layer = self.soil_layer)
                
             if obj.name == 'Bed':
                  interaction((obj.x,obj.y),(obj.width,obj.height),self.interaction_sprites,'Bed')
             

        general(
            position =  (0,0),
            surf = pygame.image.load('../graphics/world/ground.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'])

    def player_add(self,item):
         
         self.player.item_inventory[item] += 1

    def reset(self):
         
         for tree in self.tree_sprites.sprites():
              for apple in tree.apple_sprites.sprites():
                   apple.kill()
              tree.create_fruit()


    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.customize_draw(self.player)
        self.all_sprites.update(dt)
    
        self.overlay.display()

        if self.player.sleep:
             self.transition.play()

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw (self,player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(),key = lambda sprite : sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -=self.offset
                    self.display_surface.blit(sprite.image,offset_rect)

                         
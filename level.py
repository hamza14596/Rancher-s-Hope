import pygame
from settings import *
from Rancher import Player
from overlay import Overlay
from ground import general, Water
from pytmx.util_pygame import load_pygame
from help import *



class Level:
    def __init__ (self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.setup()
        self.overlay = Overlay(self.player)
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
                     general((x * TILE_SIZE,y * TILE_SIZE),surf,self.all_sprites, LAYERS['main'])


        water_frames=import_folder('../graphics/water')
        for x,y, surf in tmx_data.get_layer_by_name('Water').tiles():
            Water((x * TILE_SIZE,y * TILE_SIZE),water_frames, self.all_sprites)

          


        general(
            position =  (0,0),
            surf = pygame.image.load('../graphics/world/ground.png').convert_alpha(),
            groups =self.all_sprites ,
            z = LAYERS['ground'] )
        self.player = Player((640,360), self.all_sprites)

   
    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.customize_draw(self.player)
        self.all_sprites.update(dt)
    
        self.overlay.display()


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw (self,player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -=self.offset
                    self.display_surface.blit(sprite.image,offset_rect)
                 
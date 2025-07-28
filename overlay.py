import pygame
from settings import *

class Overlay:
    def __init__(self,player):

        self.display_surface = pygame.display.get_surface()
        self.player = player

        overlay_path ='../graphics/overlay/'
        self.tools_surf = {tools: pygame.image.load(f'{overlay_path}{tools}.png').convert_alpha() for tools in player.tools}                 
        self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seed} 

    def display(self):
        tools_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tools_surf.get_rect(midbottom = OVERLAY_POSITIONS ['tool'] ) 
        self.display_surface.blit(tools_surf,(tool_rect))
       
    
        seeds_surf = self.seeds_surf[self.player.selected_seed]
        seeds_rect = seeds_surf.get_rect(midbottom = OVERLAY_POSITIONS ['seed'] ) 
        self.display_surface.blit(seeds_surf,(seeds_rect))
       

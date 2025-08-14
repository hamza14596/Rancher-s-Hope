import pygame
from settings import *


class menu:
    def __init__(self, player, toggle_menu):

        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('font/LycheeSoda.ttf',32)

        self.width = 400
        self.space = 8
        self.padding = 10


        self.options = list(self.player.item_inventory.keys()) + list(self.player.seed_inventory.keys())
        self.sell_border = len(self.player.item_inventory) - 1
        self.setup()

    def setup(self):
        self.text_surfaces = []
        self.total_height = 0
        for item in self.options:
            text_surfaces = self.font.render(item, False, 'Black')
            self.text_surfaces.append(text_surfaces)
            self.total_height += self.text_surfaces.get_height() + (self.padding * 2)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()

    def update(self):
        self.input()
        for text_index, text_surfaces in enumerate(self.text_surfaces):
            self.display_surface.blit(text_surfaces,(100,text_index * 50))

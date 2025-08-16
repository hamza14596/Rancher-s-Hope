import pygame
from settings import *
from ticker import Ticker


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

        self.index = 0
        self.ticker = Ticker(300)

    def setup(self):
        self.text_surfaces = []
        self.total_height = 0
        for item in self.options:
            text_surfaces = self.font.render(item, False, 'Black')
            self.text_surfaces.append(text_surfaces)
            self.total_height += text_surfaces.get_height() + (self.padding * 2)

        self.total_height  += (len(self.text_surfaces) - 1) * self.space
        self.menu_top = SCREEN_HEIGHT / 2 - self.total_height / 2
        self.main_rect = pygame.Rect( SCREEN_WIDTH / 2 - self.width / 2, self.menu_top, self.width, self.total_height)

        self.buy_text = self.font.render('buy', False, 'Black')
        self.sell_text = self.font.render('sell', False, 'Black')

    def display_money(self):
        text_surface = self.font.render(f'${self.player.money}', False, 'Black')
        text_rect = text_surface.get_rect(midbottom = (SCREEN_WIDTH / 2,SCREEN_HEIGHT - 20))

        pygame.draw.rect(self.display_surface, 'White', text_rect.inflate(10,10), 0,8)
        self.display_surface.blit(text_surface,text_rect)

    def input(self):
        keys = pygame.key.get_pressed()
        self.ticker.update()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()

        
        if not self.ticker.active:
            if keys[pygame.K_UP]:
                if self.index > 0:
                    self.index -= 1
                    self.ticker.activate()

            if keys[pygame.K_DOWN]:
                if self.index < 5:
                    self.index += 1
                    self.ticker.activate()

            if keys[pygame.K_SPACE]:
                self.ticker.activate()

                current_item = self.options[self.index]
                
                if self.index <= self.sell_border:
                    if self.player.item_inventory[current_item] > 0:
                        self.player.item_inventory[current_item] -= 1
                        self.player.money +=  SALE_PRICES[current_item]



                else:
                    seed_price = SALE_PRICES[current_item]
                    if self.player.money >= seed_price:
                        self.player.seed_inventory[current_item] += 1
                        self.player.money -= PURCHASE_PRICES[current_item]

    def show_entry(self, text_surface, amount, top, selected):

        bg_rect = pygame.Rect(self.main_rect.left, top, self.width, text_surface.get_height() + self.padding * 2)
        pygame.draw.rect(self.display_surface, 'White', bg_rect, 0, 4)

        text_rect = text_surface.get_rect(midleft = (self.main_rect.left + 20, bg_rect.centery))
        self.display_surface.blit(text_surface, text_rect)

        amount_surface = self.font.render(str(amount), False ,'Black')
        amount_rect = amount_surface.get_rect(midright = (self.main_rect.right - 20, bg_rect.centery))
        self.display_surface.blit(amount_surface, amount_rect)

        if selected:
            pygame.draw.rect(self.display_surface, 'black', bg_rect,4,4)
            if self.index <= self.sell_border:
                position_rect = self.sell_text.get_rect(midleft = ( self.main_rect.left + 150,bg_rect.centery))
                self.display_surface.blit(self.sell_text,position_rect)
            else:
                position_rect = self.buy_text.get_rect(midleft = ( self.main_rect.left + 150,bg_rect.centery))
                self.display_surface.blit(self.buy_text,position_rect)
               

    def update(self):
        self.input()
        self.display_money()

        for text_index, text_surfaces in enumerate(self.text_surfaces):
            top = self.main_rect.top + text_index * (text_surfaces.get_height() + (self.padding * 2) + self.space)
            amount_list = list(self.player.item_inventory.values()) + list(self.player.seed_inventory.values())
            amount = amount_list[text_index]
            self.show_entry(text_surfaces, amount, top, self.index == text_index)

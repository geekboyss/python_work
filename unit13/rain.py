import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, test):
        super().__init__()

        self.screen = test.screen

        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self):
        # 向下移动雨滴
        self.y += 0.3
        self.rect.y = self.y

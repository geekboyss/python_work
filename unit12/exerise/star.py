import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        # 加载星星图像并设置其rect值
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        #每个星星最初在屏幕左上角
        self.rect.x = ai_game.setting.screen_width
        self.rect.y = self.rect.height
        

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """如果星星碰到了上下屏幕,返回true"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """
        向上或者向下移动外星人
        """
        self.y += (self.setting.star_speed * self.setting.fleet_direction)
        self.rect.y = self.y
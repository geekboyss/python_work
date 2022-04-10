import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理火箭发射的子弹"""
    def __init__(self, rt_game):
        super().__init__()
        self.screen = rt_game.screen
        self.setting = rt_game.setting
        self.color = self.setting.bullet_color

        # 在（0.0）处创建一个表示子弹的矩阵 并设置其正确的位置
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width,
            self.setting.bullet_height)

        self.rect.midright = rt_game.rocket.rect.midright

        self.x = float(self.rect.x)
    
    def update(self):
        self.x += self.setting.bullet_speed
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
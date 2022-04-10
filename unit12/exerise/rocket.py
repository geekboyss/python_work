import pygame

class Rocket:

    def __init__(self, test):
        self.screen = test.screen
        self.setting = test.setting

        self.screen_rect = test.screen.get_rect()

        self.image = pygame.image.load('images/rocket.bmp').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # 让飞船再屏幕左面中央
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.y > 0:
            self.y -= self.setting.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.rocket_speed
        
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)


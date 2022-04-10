import sys
import pygame

from rain import Rain

class Test:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("TestRain")

        self.rains = pygame.sprite.Group()

        self._creat_fleet()

    def display_screen(self):
        while True:
            self._check_event()
                
            self._update_rain()
            self._update_screen()
            

    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

    def _update_screen(self):
        self.screen.fill((255,255,255))
        self.rains.draw(self.screen)
        pygame.display.flip()

    def _update_rain(self):
        self.rains.update()

        Flag = False
        # 删除消失的雨滴
        for rain in self.rains.copy():
            if rain.rect.bottom >= self.screen.get_rect().bottom:
                self.rains.remove(rain)
                Flag = True

        # 如果删除了一行就在顶部创建一行
        if Flag:
            self._creat_one_line()

        print(len(self.rains))

    def _creat_one_line(self):
        rain = Rain(self)
        rain_width , rain_height = rain.rect.size

        num_rain = self.screen_width // (2 * rain_width)
        
        for num in range(num_rain):
            rain = Rain(self)
            rain.x = 2 * rain_width * num
            rain.y = rain_height;
            rain.rect.x = rain.x
            rain.rect.y = rain.y
            self.rains.add(rain)
    
    def _creat_fleet(self):
        rain = Rain(self)
        rain_width , rain_height = rain.rect.size

        num_rain = self.screen_width // (2 * rain_width)
        
        available_y = self.screen_height - 5 * rain_height
        num_row = available_y // (2 * rain_height)

        for row_num in range(num_row):
            for num in range(num_rain):
                self._creat_rain(num, row_num)

    def _creat_rain(self, rain_num, row_num):
        rain = Rain(self)
        rain_width , rain_height = rain.rect.size

        rain.x = 2 * rain_width * rain_num
        rain.y = 2 * rain_height * row_num

        rain.rect.x = rain.x
        rain.rect.y = rain.y
        self.rains.add(rain)        


if __name__ == '__main__':
    t = Test()
    t.display_screen()
import sys
import pygame

from rocket import Rocket
from settings import Setting
from bullet import Bullet
from star import Star

class Rocket_game:

    def __init__(self):
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Crazy Rocket")

        
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()

    
    def _create_fleet(self):
        star = Star(self)


        star_width, star_height = star.rect.size
        alviable_space_y = self.setting.screen_height - (2 * star_height)
        number_star_y = alviable_space_y // (2 * star_height)

        rocket_width = self.rocket.rect.width
        alviable_space_x = self.setting.screen_width - (6 * star_width) - rocket_width

        number_col = alviable_space_x // (2 * star_width)


        for col_number in range(number_col):
            for star_num in range(number_star_y):
                self._create_star(star_num, col_number)
    def _create_star(self, star_num, col_number):
            rocket_width = self.rocket.rect.width


            star = Star(self)
            star_width, star_height = star.rect.size
            star.x = (6 * star_width) + rocket_width + star_width + 2 * star_width * col_number
            star.y = star_height + 2 * star_height * star_num
            star.rect.x = star.x
            star.rect.y = star.y
            self.stars.add(star)


    def run_Rocket(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_stars()
            self._update_screen()

    def _update_stars(self):
        
        self._check_fleet_edges()
        self.stars.update()

    def _check_fleet_edges(self):
        # 有星星到边缘时采取相应措施
        for star in self.stars.sprites():
            if star.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # 将整群外星人下移，并改变其方向
        for star in self.stars.sprites():
            star.rect.x -= self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1
            
    def _update_bullets(self):
        """更新子弹位置 并删除消失的子弹"""
        # 更新子弹位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.midright > self.screen.get_rect().midright:
                self.bullets.remove(bullet)
        
        self._check_bullet_star_collisions()

    def _check_bullet_star_collisions(self):
        # 检查是否有子弹击中了星星
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.stars, False, True
        )

        # 删除现有的子弹并创建一群星星
        if not self.stars:
            self.bullets.empty()
            self._create_fleet()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.rocket.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
  

        self.stars.draw(self.screen)

        pygame.display.flip()

            
if __name__ == '__main__':
    t = Rocket_game()
    t.run_Rocket()
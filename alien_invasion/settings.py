class Setting:
    """存储设置类"""

    def __init__(self):
        """初始游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 9

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1 表示右移 -1表示左翼
        self.fleet_direction = 1



        
class Setting:
    """设置存储类"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

        # 火箭设置
        self.rocket_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 星星设置
        self.star_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 表示下移 -1 表示上移
        self.fleet_direction = 1
    
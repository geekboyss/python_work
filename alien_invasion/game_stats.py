class GameStats:

    def __init__(self, ai_game):
        # 初始化统计信息
        self.setting = ai_game.setting
        self.reset_stats()

        # 游戏启动时处于活动状态
        self.game_active = False
        # 任何情况下都不应该重置最高得分
        self.high_score = 0

    
    def reset_stats(self):
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1

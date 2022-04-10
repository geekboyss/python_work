class GameStats:

    def __init__(self, ai_game):
        self.setting = ai_game.setting
        self.reset_stats()

        # 游戏启动时处于活动状态
        self.game_active = True
        
    
    def reset_stats(self):
        self.ships_left = self.setting.ship_limit

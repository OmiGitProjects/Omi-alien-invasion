class Game_stats():
    """ Track Statistics for ALien Invasion """
    def __init__(self, setting):
        """ Initialize Statistics """
        self.setting = setting
        self.reset_stats()
        #Game Actiive Flag
        # Game In-active State
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """ Initialize Statistics that can change during the Game """
        self.ship_left = self.setting.ship_limit
        self.score = 0
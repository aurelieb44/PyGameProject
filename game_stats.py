class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False # Start Alien Invasion in an unactive state.
        self.high_score = 0 # High score should never be reset.
    
    def reset_stats(self): # Initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0 # reset score each time new game starts
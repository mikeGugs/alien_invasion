import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics.."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        # High score schould never be reset.
        self.high_score = 0
        # Update high score
        self.check_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def check_high_score(self):
        current_high_score = 'high_score.json'
        with open(current_high_score) as high:
            high_score = json.load(high)
        self.high_score = high_score
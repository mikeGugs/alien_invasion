import pygame.font
from pygame.sprite import Group
from ship import Ship
import json

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("Comic Sans", 48)
        self.label_font = pygame.font.SysFont("Comic Sans", 12)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_labels()


    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top + 5


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            high_score_json = 'high_score.json'
            with open(high_score_json, 'w') as high:
                json.dump(self.stats.score, high)
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                            self.settings.bg_color)

        # Position level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_labels(self):
        # Prep high score label
        high_score_name = "High Score"
        self.high_score_name_image = self.label_font.render(high_score_name,
                                                            True,
                                                            self.text_color,
                                                            self.settings.bg_color)
        # Place the high score label above the high score
        self.high_score_name_rect = self.high_score_name_image.get_rect()
        self.high_score_name_rect.centerx = self.high_score_rect.centerx
        self.high_score_rect.top = self.high_score_rect.top - 20

        # Prep current score label
        current_score = 'Score'
        self.current_score_image = self.label_font.render(current_score,
                                                          True,
                                                          self.text_color,
                                                          self.settings.bg_color)
        # Place the current score label above the current score
        self.current_score_label_rect = self.current_score_image.get_rect()
        self.current_score_label_rect.right = self.screen_rect.right - 20
        self.current_score_label_rect.top = self.score_rect.top - 10

        # Prep current level label
        current_level = 'Level'
        self.current_level_image = self.label_font.render(current_level,
                                                          True,
                                                          self.text_color,
                                                          self.settings.bg_color)
        # Place the current level label above the current level
        self.current_level_label_rect = self.current_level_image.get_rect()
        self.current_level_label_rect.right = self.screen_rect.right - 20
        self.current_level_label_rect.top = self.level_rect.top - 10

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def show_labels(self):
        self.screen.blit(self.high_score_name_image, self.high_score_name_rect)
        self.screen.blit(self.current_score_image, self.current_score_label_rect)
        self.screen.blit(self.current_level_image, self.current_level_label_rect)
import pygame

class GameStats:
    """ Class statistics """

    def __init__(self, game):
        """ initialize statistics """
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False
        # High score should never be reset
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """ initialize statistics that can change during the game
            We want to be able to call this method any time during the game to change the value """
        self.ship_left = self.settings.ship_limit
        # To reset stats each time a new game starts. Puts here rather than in init.
        self.score = 0

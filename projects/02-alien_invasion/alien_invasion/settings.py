import pygame

class Settings:
    """ Initialize statics settings """

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # by default move 1 pixel after each main loop. we change this behaviour here.
        # rect attributes only stores integer value.
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 400 #10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ship settings
        self.ship_limit = 3


        # Alien settings
        self.alien_speed = 5
        self.fleet_drop_speed = 20
        self.fleet_direction = 1  # 1 = right, -1 = left

        # Number of life
        self.shoot_limit = 3

        # How quickly the game speed up
        self.speedup_scale = 1.1

        # How quickly the alien points increase
        self.score_scale = 1.5


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Init settings that change thoughout the game. """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 3.0
        # Scoring
        self.alien_points = 50

        # Fleet direction of 1 represents right, -1 represent left
        self.fleet_direction = 1

    def increase_speed(self):
        """ Increase speed and alien point value settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """ Overall class for the game """

    def __init__(self):
        # Init all modules
        pygame.init()

        # Load settings
        self.settings = Settings()
        
        # Create the screen
        # It returns an object surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Create an instance of the game statistics and show the board
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Create caption
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Create the Sprite groups
        self.bullets = pygame.sprite.Group() # init the bullets group
        self.aliens = pygame.sprite.Group() # Init the aliens group

        # Create Fleet
        self._create_fleet()

        # Create button
        self.play_button = Button(self, "Play")


    def run_game(self):
        """ The main game loop """
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


    def _check_aliens_bottom(self):
        """ Check if alien has reach bottom """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat it the same way when an alien collide with a ship
                self._ship_hit()
                break


    def _ship_hit(self):
        """ Respond to a ship hit by an alien """

        if self.stats.ship_left > 0:
            # Decrement ship left and update scoreboard
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            # Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_fleet_edge(self):
        """ Respond appropriately when an alien reach the edge """
        for alien in self.aliens.sprites():
            if alien.check_edges(): # Trick, access check_edges method using this for loop
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """ Drop the entire fleet and change the fleet direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        """ Check if the fleet is at an edge
        then update the positions of all fleets """
        self._check_fleet_edge()
        self.aliens.update()

        # Look for alien-ship collision
        # take a sprite and a group as argument
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()


    def _check_events(self):
        """ Response to keypress and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # link to "event" in the for loop
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """ Start a new game when the playher hit play button """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings first
            self.settings.initialize_dynamic_settings()

            # Start the game
            self._start_game()



    def _start_game(self):
        # Reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        # Get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center it
        self._create_fleet()
        self.ship.center_ship()

        # hide the mouse cursor
        pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """ Respond to keypress. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()


    def _check_keyup_events(self, event):
        """ Response to key release """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) # Add to the group


    def _update_bullets(self):
        #  update is an actual function of pygame. 
        # It does nothing but we override it in the Bullet class
        self.bullets.update()
        
        # Get rid of the bullets that have disappear
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.check_bullet_collisions()



    def check_bullet_collisions(self):
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        ) 

        # collision return a dictionnary each time there is a collide
        # Any bullet that collides an alien becomes a key in the collistions dictionnary
        # e.g <Bullet sprite(in 0 groups)> [<Alien sprite(in 0 groups)>]
        # If we use a wide bullet, it's gonna count only 50 points. we want to change this behaviour
        # Eaxh value is a list of aliens hit by a single bullet, we multiply the number of aliens
        # in each list and add this amount to the current score
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # Empty bullet and create a new fleet if aliens group is empty
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _create_fleet(self):
        """ Create the fleet of aliens """
        # Make an alien and found the number of aliens in a row
        # Spacing between each alien is equal to one alien width

        new_alien = Alien(self)
        alien_width, alien_height = new_alien.rect.size
        new_alien_width = new_alien.rect.width
        available_space_x = self.settings.screen_width - (2 * new_alien_width) # 1 alien margin on each side
        number_aliens_x = available_space_x // (2 * new_alien_width) # 1 width for the alien and one for empty space

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height) # 1 alien from top, 2 from bottom - one ship
        number_rows = available_space_y // (2 * alien_height) 

        # Create the full raw of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)



    def _create_alien(self, alien_number, row_number):
        """ Create a fleet of aliens """
        # Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size # (x,y,width,height) size = the last two
        alien.x = alien_width + 2 * alien_width * alien_number
        
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_screen(self):
        """ Update the images on the screen and flip to the new screen """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Draw the score informations
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recent drawn visible
        pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
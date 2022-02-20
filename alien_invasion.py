import sys
from time import sleep #so we can pause the game for a moment when the ship is hit
import pygame #importing modules

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion: #manage ressources and behavior

    def __init__(self): #method to initiate the game and create resources
        pygame.init() #initializes the background settings that Pygame needs to work properly

        self.settings = Settings() #create an instance of Settings

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  #screen size
        #display window to draw graphical ele­ments
        #(1200, 800) = tuple = dimensions of the game window
        #attribute self.screen will be available in all methods in the class.
        #The object we assigned to self.screen = surface = a part of the screen where a game element can be displayed.
        #surface here = represents the entire game window.
        #use the screen_width and screen_height attributes of self.settings
        
        self.ship = Ship(self) #create an instance #self = current instance of AlienInvasion, gives Ship access to esources, screen object
        self.bullets = pygame.sprite.Group() #draw bullets to the screen on each pass through the main loop

        self.aliens = pygame.sprite.Group()
        self._create_fleet()#
        self.play_button = Button(self, "Play")  # creates instance of button with label play

        pygame.display.set_caption("Alien Invasion") #window title

        self.stats = GameStats(self) # Create an instance to store game statistics.
        self.sb = Scoreboard(self) # create scoreboard

        self.bg_color = (230,230,230) #set background color

    def run_game(self): #controls the game
        # event = action the user performs = pressing a key or moving the mouse
        # listen for events and get the right output
        while True:
            self._check_events()
            if self.stats.game_active: # happens only when game active
                self.ship.update() #calls the ship’s update() method 
                self._update_bullets()
                self._update_aliens()

            self._update_screen() #redraws screen every time you cycle
    
    def _check_events(self):
        for event in pygame.event.get(): #runs at every keyboard or mouse action
            #returns a list of events that have taken place since the last time this function was called
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #user presses key 
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #user releases key
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN: # detects MOUSEBUTTONDOWN event when player clicks anywhere 
                mouse_pos = pygame.mouse.get_pos() # returns a tuple: mouse cursor’s x- and y-coordinates when mouse button is clicked
                self._check_play_button(mouse_pos) # send values to the new method _check_play_button()

    def _check_play_button(self, mouse_pos): # Start new game when player clicks Play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) # stores true or false # check whether mouse click overlaps Play button’s rectangle
        if button_clicked and not self.stats.game_active: #game restart only if Play is clicked and game not active
            
            self.settings.initialize_dynamic_settings() # Reset the game settings. 
            
            pygame.mouse.set_visible(False) # Hide mouse cursor when no play button

            self.stats.reset_stats() # Reset game statistics = gives player 3 new ships
            self.stats.game_active = True
            self.sb.prep_score()
            self.aliens.empty() # Get rid of remaining aliens and bullets.
            self.bullets.empty()
            
            self._create_fleet() # Create a new fleet and center the ship.
            self.ship.center_ship()

    def _check_keydown_events(self, event): #helper
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT: #We can use elif blocks because each event is connected to only one key.
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #press q to exit
            sys.exit()
        elif event.key == pygame.K_SPACE: self._fire_bullet()

    def _check_keyup_events(self, event): #helper
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self): 
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self) #Creates bullet 
            self.bullets.add(new_bullet) #adds it to bullets group #like append but for pygame groups

    def _update_bullets(self):
        self.bullets.update() #update bullets' position

        for bullet in self.bullets.copy():  # Get rid of bullets that have disappeared.
            if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            #print(len(self.bullets)) #show how many bullets exist and verify they’re deleted when they reach the top
         
        self._check_bullet_alien_collisions() #call the bullet collision method
    
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True) # Check for bullets that hit aliens. If so, get rid of bullet and alien.

        if collisions: # increase score at collision alien-bullet
            for aliens in collisions.values():
                # multiply value of each alien by number of aliens in each list and add this amount to the current score
                self.stats.score += self.settings.alien_points * len(aliens) 
            self.sb.prep_score()
            

        if not self.aliens: # if zero aliens
            self.bullets.empty() # remove bullets
            self._create_fleet() # create new fleet
            self.settings.increase_speed() # increase speed when last alien shot down

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update() #updates positions of all aliens in the fleet

        if pygame.sprite.spritecollideany(self.ship, self.aliens): # Look for alien-ship collisions #returns none if no collision
            # print("Ship hit!!!")
            self._ship_hit()      

        self._check_aliens_bottom()  # Look for aliens hitting the bottom of the screen.

    def _create_fleet(self):
        alien = Alien(self) #make one instance of an alien, it won't be part of the fleet, just helps with size
        # Create an alien and find the number of aliens in a row.
        alien_width, alien_height = alien.rect.size # Spacing between each alien is equal to one alien width/height
        # get the alien’s width from its rect attribute and store this value in alien_width so no need for rect attribute
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height # Determine the number of rows of aliens that fit on the screen.
        available_space_y = (self.settings.screen_height - 
                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_rows): # Create the full fleet of aliens.
            for alien_number in range(number_aliens_x): # Create the first row of aliens.
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        alien = Alien(self) # Create an alien and place it in the row.
        alien_width, alien_height = alien.rect.size # we get the width, heigth of an alien inside the method instead of passing it as an argument. 
        alien.x = alien_width + 2 * alien_width * alien_number #Each alien is pushed to the right one alien width from the left margin.
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien) #add it to the group

    def _check_fleet_edges(self): #Respond appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self): #Respond to ship being hit by an alien
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1 # Decrement ships_left.
        
            self.aliens.empty() # Get rid of any remaining aliens and bullets.
            self.bullets.empty()

            self._create_fleet() # Create a new fleet and center the ship.
            self.ship.center_ship()
        
            sleep(0.5) # Pause for 0.5 seconds
        else:
            self.stats.game_active = False # user has used up all their ships
            pygame.mouse.set_visible(True) # make cursor reappear once game ends so player can click Play

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit() # Treat this the same as if the ship got hit.
                break

    def _update_screen(self): #Update screen image and switch to new screen
        self.screen.fill(self.settings.bg_color) #fill the screen after each loop
        self.ship.blitme() #draw the ship
        for bullet in self.bullets.sprites():  #method returns a list of all sprites in the group bullet
            bullet.draw_bullet() #draw fire bullets
        self.aliens.draw(self.screen) #make the alien appear
        self.sb.show_score() # draw scoreboard
        
        if not self.stats.game_active: # Draw the play button if the game is inactive.
            self.play_button.draw_button()
        pygame.display.flip() #display the new positions of game elements, hides old ones

if __name__ == '__main__': #check for special variables, which is set during program execution
    ai = AlienInvasion()
    ai.run_game() #create an instance




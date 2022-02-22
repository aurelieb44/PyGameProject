import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game): # Initialize scorekeeping attributes
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30) # font settings for scoring info
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score() # call text to be displayed as image
        self.prep_high_score() # display high score separately
        self.prep_level() # display current level
        self.prep_ships()

    def prep_score(self): # Turn the score into a rendered image
        score_str = str(self.stats.score) # turn numerical value stats.score into a string
        # pass string to render(), which creates the image
        # to display the score clearly onscreen, pass screen’s background color and text color to render().
        
        rounded_score = round(self.stats.score, -1) # round to the nearest 10
        score_str = "{:,}".format(rounded_score) # insert commas into numbers when converting a numerical value to a string
        
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color) 
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect() # create rect, score lines up with right side of screen
        self.score_rect.right = self.screen_rect.right - 20 # 20 pixels from the right edge of the scree
        self.score_rect.top = 20 # place the top edge 20 pixels down from the top of the screen

    def show_score(self): # draw score to screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen) # draw ships

    def prep_high_score(self): # Turn high score into a rendered image
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color) # generate image from high score
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self): # Check to see if there's a new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score() # call to update the high score’s image

    def prep_level(self): # Turn value stored in stats.level into a rendered image
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
            self.text_color, self.settings.bg_color) 

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right # sets image’s right attribute to match score’s right attribute
        self.level_rect.top = self.score_rect.bottom + 10 # sets the top attribute 10 pixels beneath the bottom of the score image

    def prep_ships(self): #Show how many ships are left
        self.ships = Group() # empty group to hold ship instances
        for ship_number in range(self.stats.ships_left): # loop for every ship left
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width # 10 pixels margin between ships
            ship.rect.y = 10 # ships appear on upper-left corner
            self.ships.add(ship) # add new ship to the group
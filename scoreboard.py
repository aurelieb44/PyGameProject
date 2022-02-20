import pygame.font

class Scoreboard:
    def __init__(self, ai_game): # Initialize scorekeeping attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30) # font settings for scoring info
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score() # call text to be displayed as image

    def prep_score(self): # Turn the score into a rendered image
        score_str = str(self.stats.score) # turn numerical value stats.score into a string
        # pass string to render(), which creates the image
        # to display the score clearly onscreen, pass screen’s background color and text color to render().
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color) 
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect() # create rect, score lines up with right side of screen
        self.score_rect.right = self.screen_rect.right - 20 # 20 pixels from the right edge of the scree
        self.score_rect.top = 20 # place the top edge 20 pixels down from the top of the screen

    def show_score(self): # draw score to screen
        self.screen.blit(self.score_image, self.score_rect)
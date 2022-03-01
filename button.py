import pygame.font  #modulelets Pygame render text

class Button:
    def __init__(self, ai_game, msg): # Initialize button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
    
        self.width, self.height = 200, 50 # dimensions and properties of the button.
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) # None: default font, size of the text

        self.rect = pygame.Rect(0, 0, self.width, self.height) # Build the button's rect object and center it.
        self.rect.center = self.screen_rect.center  # set center attribute to match that of the scree

        self._prep_msg(msg) # The button message needs to be prepped only once.

    def _prep_msg(self, msg): # Turn msg into a rendered image and center text on the button.
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color) # font.render turns msg into image which we then store in self.msg_image
        # center the text image on the button by creating a rect from the image and setting its center attribute to match that of the button.
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center 

    def draw_button(self): # display button on screen
        self.screen.fill(self.button_color, self.rect) # draw rectangle
        self.screen.blit(self.msg_image, self.msg_image_rect) # draw the text image
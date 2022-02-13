import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect() #set rect attribute.
        
        self.rect.x = self.rect.width # Start each new alien near the top left of the screen.
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x) # Store the alien's exact horizontal position.

    def check_edges(self):
        screen_rect = self.screen.get_rect() 
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True # Return True if alien is at edge of screen

    def update(self):
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction) #moves alien to the right # track position
        self.rect.x = self.x #update position
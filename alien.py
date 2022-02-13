import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect() #set rect attribute.
        
        self.rect.x = self.rect.width # Start each new alien near the top left of the screen.
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x) # Store the alien's exact horizontal position.
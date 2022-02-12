import pygame

class Ship:

    def __init__(self, ai_game): #starting position of the ship
        self.screen = ai_game.screen #assign the screen to an attribute of Ship, so we can access it easily
        self.screen_rect = ai_game.screen.get_rect() #access the screen’s rect attribute & place the ship in the correct location on the screen.
        
        self.image = pygame.image.load('ship.bmp') # returns a surface representing the ship
        self.rect = self.image.get_rect() #get external rectangle of the ship 

        self.rect.midbottom = self.screen_rect.midbottom #where to position new ship

    def blitme(self):
        self.screen.blit(self.image, self.rect) #draw the ship at its current location
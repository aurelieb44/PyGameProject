import pygame

class Ship:

    def __init__(self, ai_game): #starting position of the ship
        self.screen = ai_game.screen #assign the screen to an attribute of Ship, so we can access it easily
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #access the screen’s rect attribute & positions the ship
        
        self.image = pygame.image.load('ship.bmp') # returns a surface representing the ship
        self.rect = self.image.get_rect() #get external rectangle of the ship 

        self.rect.midbottom = self.screen_rect.midbottom #where to position new ship
        self.x = float(self.rect.x)  # Store a decimal value for the ship's position.
         
        self.moving_right = False # Movement flag
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect) #draw the ship at its current location 

    def update(self): #update ship's position based on movement flag #call through an instance of the ship #not helper method
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left: #we don't use elif to be more accurate when user holds both keys
            self.rect.x -= 1

#    def update(self):
#         if self.moving_right and self.rect.right < self.screen_rect.right:
#             self.x += self.settings.ship_speed
#         elif self.moving_left and self.rect.left > 0:
#             self.x -= self.settings.ship_speed
#         self.rect.x = self.x  # Update rect value
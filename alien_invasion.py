import sys
import pygame #importing modules

from settings import Settings
from ship import Ship

class AlienInvasion: #manage game assets and behavior

    def __init__(self): #method to initiate the game and create resources
        pygame.init() #initializes the background settings that Pygame needs to work properly

        self.settings = Settings() #create an instance of Settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        #display window to draw graphical ele­ments
        #(1200, 800) = tuple that defines the dimensions of the game window
        #attribute self.screen will be available in all methods in the class.
        #The object we assigned to self.screen = surface = a part of the screen where a game element can be displayed.
        #surface here = represents the entire game window.
        #use the screen_width and screen_height attributes of self.settings
        pygame.display.set_caption("Alien Invasion") 

        self.ship = Ship(self) #create an instance #self = current instance of AlienInvasion, gives Ship access to esources, screen object

        self.bg_color = (230,230,230) #set background color

    def run_game(self): #controls the game
        # event = action the user performs = pressing a key or moving the mouse
        # listen for events and get the right output
        while True:
            for event in pygame.event.get(): #runs at every keyboard or mouse action
            #returns a list of events that have taken place since the last time this function was called
                if event.type == pygame.QUIT:
                    sys.exit

            self.screen.fill(self.settings.bg_color) #fill the screen after each loop

            self.ship.blitme() #draw the ship
            
            pygame.display.flip() #display the new positions of game elements, hides old ones

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game() #create an instance




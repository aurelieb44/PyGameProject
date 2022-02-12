import pygame
from pygame.sprite import Sprite
   
class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__() #create bullet object at ship's position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, # Create a bullet rect at (0, 0) and then set correct position
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop #bullet’s midtop attribute to match ship’s midtop attri­bute. bullet emerge from ship

        self.y = float(self.rect.y)  # Store the bullet's position as a decimal value

    def update(self):
        self.y -= self.settings.bullet_speed # Update bullet decimal position
        self.rect.y = self.y # Update rect position.

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
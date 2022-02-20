class Settings: #work with just one settings object any time we access one setting

    def __init__(self):
        self.screen_width = 1200 #screen settings
        self.screen_height = 600
        self.bg_color = (230,230,230)

        self.ship_limit = 3 # number of ships player starts with

        #alien settings
        self.fleet_drop_speed = 100 # how quickly fleet drops down each time an alien reaches either edge

        # Bullet settings
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5 # How quickly the alien point values increase
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self): # settings that change during the game
        self.ship_speed = 1.5 # moves by 1.5 pixels
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # include fleet _direction so aliens always move right at the beginning of a new game. 
        self.fleet_direction = 1 # fleet_direction of 1 represents right; -1 represents left.

        self.alien_points = 50 # scoring # make sure point value is reset each time new game starts

    def increase_speed(self): # multiply each speed by value of speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points) # see value of each alien
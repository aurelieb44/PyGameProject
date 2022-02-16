class Settings: #work with just one settings object any time we access one setting

    def __init__(self):
        self.screen_width = 1200 #screen settings
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5 #moves by 1.5 pixels
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # how quickly fleet drops down each time an alien reaches either edge
        self.fleet_direction = 1 # fleet_direction of 1 represents right; -1 represents left.

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
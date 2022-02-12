class Settings: #work with just one settings object any time we access one setting

    def __init__(self):
        self.screen_width = 1200 #screen settings
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5 #moves by 1.5 pixels

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
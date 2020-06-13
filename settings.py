class Settings():
    def __init__(self):
        self.field_width = 100
        self.field_height = 100
        self.x_fields = 10
        self.y_fields = 10
        self.screen_width = self.field_width * self.x_fields
        self.screen_height = self.field_height * self.y_fields
        self.bg_color = (255, 255, 255)

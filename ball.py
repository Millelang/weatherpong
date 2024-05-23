import pygame
from object import object

class Ball(object):
    

        def update(self):
        # Kollar vilken kant bollen är i kontakt med och ändrar riktning eller "resettar rundan"
            if self.y > 500 or self.y < 0:
                self.speed_y *= -1
            if self.x > 700 or self.x < 0:
                self.x = 350
                self.y = 250
            print(self.x, self.y)
            self.x += self.speed_x
            self.y += self.speed_y

import pygame
class intersect:

    ## funktion som kollar om två objekt krockar
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
    def check(self):
        if self.obj1.x < self.obj2.x + self.obj2.width and self.obj1.x + self.obj1.width > self.obj2.x and self.obj1.y < self.obj2.y + self.obj2.height and self.obj1.y + self.obj1.height > self.obj2.y:
            return True
        else:
            return False
import math

class Point:
    def __init__(self, x=None, y=None):
        self.x = int(math.sqrt(x ** 2))
        self.y = int(math.sqrt(y ** 2))
    


class Field:
    def __init__(self, points):
        self.field = points

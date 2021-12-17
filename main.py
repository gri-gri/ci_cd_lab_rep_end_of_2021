import math

class Point:
    def __init__(self, x=None, y=None):
        self.x = int(math.sqrt(x ** 2))
        self.y = y
    


class Field:
    def __init__(self, points):
        self.field = points

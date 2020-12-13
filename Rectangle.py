from Point import Point 
from Polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, p1, p2, p3, p4):
        self.a = p1
        self.b = p2
        self.c = p3
        self.d = p4

    def __str__(self):
        return f'[{self.a}, {self.b}, {self.c}, {self.d}]'

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d:
            return True
        return False

    def sortPoints(self):
        list = [[self.a.x, self.a.y], [self.b.x, self.b.y], [self.c.x, self.c.y], [self.d.x, self.d.y]]
        list.sort()
        self.a = Point(list[0][0], list[0][1])
        self.b = Point(list[1][0], list[1][1])
        self.c = Point(list[2][0], list[2][1])
        self.d = Point(list[3][0], list[3][1])

    
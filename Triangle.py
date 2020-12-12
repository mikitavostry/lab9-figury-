import math
from Point import Point
from Figure import Figure
class Triangle(Figure):
    def __init__(self, p1, p2, p3):
        self.a = p1
        self.b = p2
        self.c = p3

    def __str__(self):
        return f'[{self.a}, {self.b}, {self.c}]'

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return True
        return False

    def find_area(self):
        side_1 = math.sqrt((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2)
        side_2 = math.sqrt((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2)
        side_3 = math.sqrt((self.a.x - self.c.x) ** 2 + (self.a.y - self.c.y) ** 2)
        perimeter = (side_1 + side_2 + side_3) / 2
        if perimeter - side_1 > 0 and perimeter - side_2 > 0 and perimeter - side_3 > 0:
            area = math.sqrt(perimeter * (perimeter - side_1) *
                        (perimeter - side_2) * (perimeter - side_3))
            return area
        else:
            return 0

    def sortPoints(self):

        list = [[self.a.x, self.a.y], [self.b.x, self.b.y], [self.c.x, self.c.y]]

        list.sort()
        
        self.a = Point(list[0][0], list[0][1])
        self.b = Point(list[1][0], list[1][1])
        self.c = Point(list[2][0], list[2][1])
class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

class PointValueError(Exception):
    pass
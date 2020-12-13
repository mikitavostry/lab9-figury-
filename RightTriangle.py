from Triangle import Triangle
class RightTriangle(Triangle):
    
    def isPointInside(self, point):
        tr_area = float(format(self.find_area(), '.3f'))
        tr1 = Triangle(self.a, self.b, point)
        tr2 = Triangle(self.a, self.c, point)
        tr3 = Triangle(self.b, self.c, point)
        p1 = float(format(tr1.find_area(), '.3f'))
        p2 = float(format(tr2.find_area(), '.3f'))
        p3 = float(format(tr3.find_area(), '.3f'))
        if tr_area == p1 + p2 + p3:
            return True
        return False
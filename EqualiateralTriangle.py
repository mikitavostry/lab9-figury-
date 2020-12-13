from Triangle import Triangle
class EqualiateralTriangle(Triangle):
    
    def is_point_inside(self, p):
        p1 = self.a
        p2 = self.b
        p3 = self.c

        #Zamieniamy na współrzędne barycentrzyczne
        alpha = ((p2.y - p3.y)*(p.x - p3.x) + (p3.x - p2.x)*(p.y - p3.y)) / ((p2.y - p3.y)*(p1.x - p3.x) + (p3.x - p2.x)*(p1.y - p3.y))

        beta = ((p3.y - p1.y)*(p.x - p3.x) + (p1.x - p3.x)*(p.y - p3.y)) / ((p2.y - p3.y)*(p1.x - p3.x) + (p3.x - p2.x)*(p1.y - p3.y))

        gamma = 1.0 - alpha - beta

        #jeżeli wszystkie współrzędne są większe od 0 to znaczy, że dany punkt znajduje się w środku trójkąta 
        if(gamma > 0 and beta > 0 and alpha > 0):

            return True

        else:

            return False
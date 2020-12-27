import math
from Rectangle import Rectangle
from RightTriangle import RightTriangle
from EqualiateralTriangle import EqualiateralTriangle
from Point import Point

class Searcher:
    @staticmethod
    def searchForSquares(points):
        foundSquares = []

        for point in points:

            for secondPoint in points:
                if secondPoint == point:
                    continue

                if secondPoint.x == point.x:
                    squareSize = secondPoint.y - point.y

                    if squareSize < 0:
                        continue

                    desiredPoint = Point(secondPoint.x + squareSize, secondPoint.y)

                    if desiredPoint in points:
                        secondDesiredPoint = Point(point.x + squareSize, point.y)

                        if secondDesiredPoint in points:
                            square = Rectangle(point, secondPoint, desiredPoint, secondDesiredPoint)
                            square.sortPoints()
                            if square not in foundSquares:
                                foundSquares.append(square)

        goodSquares = []
        for square in foundSquares:
            isGoodSquare = True
            for point in points:
                if square.is_point_inside(point):
                    isGoodSquare = False
                    break
            if isGoodSquare:
                goodSquares.append(square)

        return goodSquares

    @staticmethod
    def serchForRightEmptyTriangle(points):
        two_points = []
        for point1 in points:
            for point2 in points:
                if point1 != point2 and point1.x == point2.x:
                    two_points.append([point1, point2])
        right_triangles = []
        for a in two_points:
            for b in points:
                if b != a[0] and b.y == a[0].y:
                    copy = a[:]
                    copy.append(b)
                    right_triangles.append(RightTriangle(copy[0], copy[1], copy[2]))
        empty_triangles = []
        for trngl in right_triangles:
            flag = True
            for point in points:
                if trngl.a != point and trngl.b != point and trngl.c != point \
                        and trngl.is_point_inside(point):
                    flag = False
                    break
            if flag:
                empty_triangles.append(trngl)
        return empty_triangles
        


    @staticmethod
    def findLengthBetweenTwoPoints(point1, point2):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
        
    @staticmethod
    def searchForEmptyEquilateralTriangle(points):
        goodTriangles = []


        for point in points:
        
            for point2 in points:

                if(point.x != point2.x and point.y != point2.y):

                    for point3 in points:

                        #liczymy długości boków
                        distA = round(Searcher.findLengthBetweenTwoPoints(point3, point), 1)
                        distB = round(Searcher.findLengthBetweenTwoPoints(point3, point2), 1)
                        distC = round(Searcher.findLengthBetweenTwoPoints(point, point2), 1)

                        #jeżeli długości boków są takie same, wtedy mamy doczynienia z trójkątem równobocznym
                        if(distA == distB and distB == distC):

                            EqTrinagle = EqualiateralTriangle(point, point2, point3)
                            
                            #sortujemy punkty po to żeby wyeliminować powtórzenie się trójkąta ze zmienioną kolejnością punktów
                            EqTrinagle.sortPoints()

                            if EqTrinagle not in goodTriangles:
                                
                                #zakładamy, że w środku nie ma żadnego punktu
                                isEmpty = True

                                for newpoint in points:

                                    #sprawdzamy pokolei czy któryś z punktów przypadkiem nie znajduje sie w srdoku naszego trójkąta
                                    if(EqTrinagle.is_point_inside(newpoint)):

                                        #znalazło punkt w środku
                                        isEmpty = False

                                #jeżeli trójkąt jest pusty wpisujemy go do listy
                                if isEmpty is True:

                                    goodTriangles.append(EqTrinagle)



        return goodTriangles

    @staticmethod
    def searchForRectangle(points):
        foundRectangles = []

        for point in points:

            for secondPoint in points:
                if secondPoint == point:
                    continue

                if secondPoint.x == point.x:
                    y = secondPoint.y - point.y

                    if y < 0:
                        continue

                    for thirdPoint in points:
                        if thirdPoint == point or thirdPoint == secondPoint:
                            continue

                        if thirdPoint.y == point.y:
                            x = thirdPoint.x - point.x

                            if x < 0 or x == y:  # Odrzucam kwadraty
                                continue

                            desiredPoint = Point(secondPoint.x + x, thirdPoint.y + y)

                            if desiredPoint in points:
                                rectangle = Rectangle(point, secondPoint, thirdPoint, desiredPoint)
                                rectangle.sortPoints()
                                if rectangle not in foundRectangles:
                                    foundRectangles.append(rectangle)
        emptyRectangles = []
        for rectangle in foundRectangles:
            if Searcher.searchForPointsInsideRectangle(rectangle, points):
                emptyRectangles.append(rectangle)
        return emptyRectangles

    @staticmethod
    def searchForPointsInsideRectangle(rectangle, points):
        for point in points:
            if point == rectangle.a or point == rectangle.b or point == rectangle.c or point == rectangle.d:
                continue
            if (rectangle.a.y <= point.y <= rectangle.b.y) and (rectangle.a.x <= point.x <= rectangle.c.x):
                return False
        return True


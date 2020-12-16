from Parser import Parser
from Searcher import Searcher

if __name__ == "__main__":
    points = Parser.inputParser(input('Podaj współrzędne punktów \n'))

    foundSquares = Searcher.searchForSquares(points)
    print('Znalezione kwadraty: ')
    for square in foundSquares:
        print(square)

    foundRectangles = Searcher.searchForRectangle(points)
    print('Znalezione prostokąty: ')
    for rectangle in foundRectangles:
        print(rectangle)

    triangles = Searcher.serchForRightEmptyTriangle(points)
    print('Znalezione trójkąty prostokątne: ')
    for triangle in triangles:
        print(triangle)

    Equilateraltriangles = Searcher.searchForEmptyEquilateralTriangle(points)
    print('Znalezione trójkąty równoboczne: ')
    for Equilateraltriangle in Equilateraltriangles:
        print(Equilateraltriangle)

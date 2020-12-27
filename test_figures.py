import pytest
from Triangle import *
from Point import *
from Searcher import *
from RightTriangle import *
def test_create_triangle():
    triangle = Triangle(Point(1, 1), Point(1, 3), Point(3, 3))
    assert triangle.a == Point(1, 1)
    assert triangle.b == Point(1, 3)
    assert triangle.c == Point(3, 3)

def test_incorrect_point_value():
    with pytest.raises(PointValueError):
        triangle = Triangle(Point(1, 2), (2, 3), Point(3, 2))

def test_is_point_inside():
    assert RightTriangle(Point(1, 1), Point(1, 3), Point(3, 3)).is_point_inside(Point(1.2, 2.9)) == True
    assert RightTriangle(Point(1, 1), Point(1, 3), Point(3, 3)).is_point_inside(Point(3, 5)) == False





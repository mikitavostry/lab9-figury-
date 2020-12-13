from abc import ABC, abstractmethod

class Polygon(ABC):

    def find_area(self):
        pass

    @abstractmethod
    def is_point_inside(self, point):
        pass

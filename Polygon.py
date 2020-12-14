from abc import ABC, abstractmethod

class Polygon(ABC):

    def find_area(self):
        pass

    @abstractmethod
    def is_point_inside(self, point):
        pass

    def print_info(self):
        print('Obiekt typu ' + type(self).__name__ + '\nwyznaczony przez punkty '
              + str(self) + '\no polu równym ' + str(self.find_area()))
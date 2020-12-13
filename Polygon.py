import abc

class Polygon(object):
    __metaclass__=abc.ABCMeta

    @abc.abstractmethod
    def find_area(self):
        pass

    @abc.abstractmethod
    def is_point_inside(self, point):
        pass

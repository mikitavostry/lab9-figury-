import re
from Point import Point
class Parser:
    @staticmethod
    def inputParser(str):
        userInput = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", str)
        if len(userInput) % 2 != 0:
            del userInput[len(userInput) - 1]
        points = []
        for i in range(0, len(userInput), 2):
            points.append(Point(float(userInput[i]), float(userInput[i + 1])))
        return points
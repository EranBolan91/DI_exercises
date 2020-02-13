import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    @staticmethod
    def compute_area(r):
        return math.pi * r ** 2


if __name__ == '__main__':
    c = Circle(radius=2)
    print(c.area())
    print(c.compute_area(5))


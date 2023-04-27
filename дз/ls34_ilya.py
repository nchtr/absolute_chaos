#1
from math import pi

class Cylinder:
    def __init__(self, diametr, height) -> None:
        self._diametr = diametr
        self._height = height
        self._area = self.calcArea(diametr, height)

    @staticmethod
    def calcArea(di, h):
        circle = pi * di ** 2 / 4
        side = pi * di * h
        return round(circle*2 + side, 2)

    def __setattr__(self, name, value):
        if name in ['_diametr', '_height']:
            self.__dict__[name] = value
            self._area = self.calcArea(self._diametr, self._height)
        elif name == '_area':
            raise AttributeError("can't set attribute")
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == '_area':
            return self.calcArea(self._diametr, self._height)
        else:
            return self.__dict__[name]

    @property
    def diametr(self):
        return self._diametr

    @diametr.setter
    def diametr(self, value):
        self._diametr = value
        self._area = self.calcArea(self._diametr, self._height)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._area = self.calcArea(self._diametr, self._height)

    @property
    def area(self):
        return self._area




#2
class Geometry:
    def __init__(self) -> None:
        self._count = 0
    
    @staticmethod
    def triangle_area(a, b, c):
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
    @staticmethod
    def rectangle_area(a, b):
        return a * b
    
    @staticmethod
    def square_area(a):
        return a ** 2
    
    @staticmethod
    def rhombus_area(d1, d2):
        return (d1 * d2) / 2
    
    @staticmethod
    def get_count():
        return Geometry._count
    
    def __init__(self):
        Geometry._count += 1
        
        
        
#3
class Math:
    @staticmethod
    def max_of_four(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_of_four(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average_of_four(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Math.factorial(n-1)


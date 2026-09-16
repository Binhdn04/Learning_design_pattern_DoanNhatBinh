# Lớp con phải có khả năng thay được lớp cha (child classess are able to replace their parent classess)
from abc import ABC, abstractmethod

class Rectangle(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @abstractmethod
    def area(self):
        return self._width * self._height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    @abstractmethod
    def set_width(self, width):
        self._width = width 
    @abstractmethod
    def set_height(self, height):
        self._height = height

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def set_width(self, width):
        self._width = self._height = width

    def set_height(self, height):
        self._width = self._height = height 

    def area(self):
        return self._width * self._height

s = Square(5)
s.set_height(10)
print(f"Area: {s.area()}")
from abc import ABC, abstractmethod
from math import pi

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print_area(self):
        pass

class Triangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2

    def print_area(self):
        print(f"El área del triángulo es {self.area()}")

class Rectangle(Polygon):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def print_area(self):
        print(f"El área del rectángulo es {self.area()}")

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
    def print_area(self):
        print(f"El área del cuadrado es {self.area()}")

class Circle(Polygon):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
    
    def print_area(self):
        print(f"El área del circulo es {self.area()}")

def area(polygon):
    polygon.print_area()
    return polygon.area()


# Ponemos a prueba
triangulo = Triangle(4, 4)
rectangulo = Rectangle(4, 4)
cuadrado = Square(5)
circulo = Circle(5)

area(triangulo)
area(rectangulo)
area(cuadrado)
area(circulo)
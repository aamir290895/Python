from abc import ABC, abstractmethod

# Define an abstract base class (interface) called 'Shape'
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Implement a concrete class 'Circle' that inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Implement another concrete class 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating instances and using the interface methods
circle_instance = Circle(radius=5)
rectangle_instance = Rectangle(length=4, width=6)

print("Circle - Area:", circle_instance.area())
print("Circle - Perimeter:", circle_instance.perimeter())

print("Rectangle - Area:", rectangle_instance.area())
print("Rectangle - Perimeter:", rectangle_instance.perimeter())

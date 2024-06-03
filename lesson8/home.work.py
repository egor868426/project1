class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password


user = User("Tom Toms", "Tom.Toms@icloud.com", "password_557")

print("Name:", user.get_name())
print("Email:", user.get_email())
print("Password:", user.get_password())






from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

circle = Circle(5)
rectangle = Rectangle(5, 5)
triangle = Triangle(6, 1)

print("Circle area:", circle.calculate_area())
print("Rectangle area:", rectangle.calculate_area())
print("Triangle area:", triangle.calculate_area())

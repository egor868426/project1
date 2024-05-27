class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

def make_sound(self):
     return f"{self.name} make a sound."
animal1 = Animal("Bob", "Dog", 5)











class Rectangle:
    def __init__(self, width, height):
         self.width = width
         self.height = height

    def area(self):
         return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    rectangle = Rectangle(10, 20)
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")


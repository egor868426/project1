class Person:
    name = "Tom"
    age = 18


print(Person.name, Person.age)
Person.age = 50
print(Person.name, Person.age)
print(Person.__dict__)








class Person:
    """Class for criation persons"""
    name = "Tom"
    age = 18
    high = 180

person1 = Person()

del Person.high
print(Person.__dict__)
print(hasattr(Person, "high"))

delattr(Person, "age")
print(Person.__dict__)
print(hasattr(Person, "age"))



print(Person.__doc__)







class Person:
    """Class for criation persons"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attrs(self):
        print(f">>>> {self} <<<<")
        print(self.name, self.age)


person1 = Person("Tom", 18)
print(person1)
person1.print_attrs()


person2 = Person("Oleg", 50)
print(person2)
person2.print_attrs()











class Point:
    """Class for create and set coords"""

    def __init__(self, x, y, z) -> None:
       self.x = x
       self.y = y
       self.z = z
       self.get_attrs()
       self.check_coords()

    def check_coords(self):
        for attr in self.__dict__:
            if getattr(self, attr, False) < 0 and not isinstance(self.__dict__[attr], str):
                print("coord can't be less than 0")
                getattr(self, attr, 0)
            elif getattr(self, attr, False) > 100  and not isinstance(self.__dict__[attr], str):
                print("coord can't be great than 100")
                getattr(self, attr, 100)
        print(self.__dict__)

    def get_attrs(self):
        print(self.__dict__)

    def set_attrs(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(self.__dict__)


coord_1: Point = Point(-1, 101, 50)

print("----------")
coord_1.set_attrs(1000, 1000, 5)



from abc import ABC, abstractmethod
# Python provides a module named abc which allows you to create abstract base classes. These classes can have abstract methods that must be overridden by subclasses.
#
# In this example, the Shape class is defined as an abstract base class using the ABC metaclass. The @abstractmethod decorator ensures that any concrete subclass of Shape must implement the area() method.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

obj = Circle(2)
print(obj.area())
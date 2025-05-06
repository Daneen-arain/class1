import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example
c = Circle(7)
print("Area:", c.area())            # Output: Area: 153.94...
print("Perimeter:", c.perimeter())  # Output: Perimeter: 43.98...

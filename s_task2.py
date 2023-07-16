class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None else width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10)
print("Периметр прямоугольника:", rectangle.perimeter(), "Площадь прямоугольника:", rectangle.area())


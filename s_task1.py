# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math
class Circle():

    def __init__(self,radius) -> None:
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2
    
circle_1 = Circle(5)

print("Длина окружности:",circle_1.circumference(), "Площадь окружности:", circle_1.area())
   
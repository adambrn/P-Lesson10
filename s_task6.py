# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def info(self):
        return f"Животное: {self.name}\nВид: {self.animal_type}\n"


class Fish(Animal):
    def __init__(self, name, animal_type, water_type):
        super().__init__(name, animal_type)
        self.water_type = water_type

    def info(self):
        return super().info() + f"Тип воды: {self.water_type}\n"


class Bird(Animal):
    def __init__(self, name, animal_type, can_fly):
        super().__init__(name, animal_type)
        self.can_fly = can_fly

    def info(self):
        return super().info() + f"Может летать: {self.can_fly}\n"


class Mammal(Animal):
    def __init__(self, name, animal_type, habitat):
        super().__init__(name, animal_type)
        self.habitat = habitat

    def info(self):
        return super().info() + f"Место обитания: {self.habitat}\n"

fish = Fish('Оранжевый амфиприон', 'Рыба-клоун', 'Соленая')
bird = Bird('Ара', 'Попугай', True)
mammal = Mammal('Лев', 'Кошачьи', 'Саванна')

print(fish.info(), bird.info(), mammal.info(), sep='\n')

# Доработаем задачи 5-6. Создайте класс-фабрику. 
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

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


class AnimalFactory:
    def create_animal(self, animal_type, name, *args):
        if animal_type == "Fish":
            return Fish(name, *args)
        elif animal_type == "Bird":
            return Bird(name, *args)
        elif animal_type == "Mammal":
            return Mammal(name, *args)
        else:
            return ValueError("Неподдерживаемый тип животного")


animal_factory = AnimalFactory()

fish = animal_factory.create_animal("Fish", "Оранжевый амфиприон", "Рыба-клоун", "Соленая")
bird = animal_factory.create_animal("Bird", "Ара", "Попугай", True)
mammal = animal_factory.create_animal("Mammal", "Лев", "Кошачьи", "Саванна")
snake = animal_factory.create_animal("Snake", "Змея", "Ползучие", "Морская")

print(fish.info(), bird.info(), mammal.info(), snake, sep='\n')

# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name, type, water_type):
        self.name = name
        self.type = type
        self.water_type = water_type

    def info(self):
        return f"Рыба: {self.name}\nВид: {self.type}\nТип воды: {self.water_type}\n"

class Bird:
    def __init__(self, name, type, can_fly):
        self.name = name
        self.type = type
        self.can_fly = can_fly

    def info(self):
        return f"Птица: {self.name}\nВид: {self.type}\nМожет летать: {self.can_fly}\n"



class Mammal:
    def __init__(self, name, type, habitat):
        self.name = name
        self.type = type
        self.habitat = habitat

    def info(self):
        return f"Млекопитающее: {self.name}\nВид: {self.type}\nМесто обитания: {self.habitat}\n"
  

fish = Fish('Оранжевый амфиприон', 'Рыба-клоун', 'Соленая')
bird = Bird('Ара', 'Попугай', True)
mammal = Mammal('Лев', 'Кошачьи', 'Саванна')

print(fish.info(), bird.info(), mammal.info(), sep = '\n')

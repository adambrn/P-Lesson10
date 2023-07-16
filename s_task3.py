# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Cвойство возраст должно быть недоступно для прямого обращения, но возможность получить текущий возраст должна присутствовать.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        return self._age

if __name__ == 'main':
    person = Person("Дарт", "Вейдер", 45)
    person.birthday()

    print("Полное имя:", person.full_name(), "Текущий возраст:", person.get_age(),)

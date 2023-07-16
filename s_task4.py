# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания. Используйте импорт класса в новый файл.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь

from s_task3 import Person

class Employee(Person):
    def __init__(self, first_name, last_name, age, id_number):
        super().__init__(first_name, last_name, age)
        self.id_number = id_number
        self._access_level = self.id_number % 7

    def get_access_level(self):
        return self._access_level
        
    
employee = Employee("Люк", "Скайуокер", 33, 3332223)

print("Полное имя сотрудника:", employee.full_name(), "Уровень доступа:", employee.get_access_level())

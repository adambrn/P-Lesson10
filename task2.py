# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. 
# Превратите функции в методы класса. 
# Задачи должны решаться через вызов методов экземпляра. 

""" 1. Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции """

import random

class FileFiller:
    def __init__(self, file_name, num_lines):
        self.file_name = file_name
        self.num_lines = num_lines

    def fill_file_with_random_pairs(self):
        START, END = -1000, 1000

        with open(self.file_name, 'a') as file:
            for _ in range(self.num_lines):
                file.write(f"{random.randint(START, END)}|{random.uniform(START, END)}\n")

if __name__ == '__main__':
    filler = FileFiller("numbers.txt", 10)
    filler.fill_file_with_random_pairs()

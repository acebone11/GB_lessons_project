# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    pass


class OfficeEqipment:
    def __init__(self, name, price, func):
        self.name = name
        self.price = price
        self.func = func
        self.items = {'Модель устройства ': self.name, 'Цена устройства ': self.price, 'Функция устройства ':self.func}

    def income(self):
        self.name = input('Введите название устройства ')
        self.price = float(input('Введите цену устройства'))
        self.func = input('Введите функцию устройства')
        item = {'Модель устройства ': self.name, 'Цена устройства ': self.price, 'Функция устройства ': self.func}
        self.items.update(item)
class Printer(OfficeEqipment):
    def to_print(self):
        return 'печатаю'

class Scanner(OfficeEqipment):
    def Scan(self):
        return 'Сканирую'

class Xerox(OfficeEqipment):
    def xerox(self):
        return 'Копирую'



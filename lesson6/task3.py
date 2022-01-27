# Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position
# (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на
# реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать
# методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.positon = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' '+ self.surname

    def income_person(self):
        return self.income.get('wage') + self.income.get('bonus')


a = Position('Peter' , 'Parker', 'Spiderman', 100000, 25000)
print(a.get_full_name())
print(a.positon)
print(a.income_person())

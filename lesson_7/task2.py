# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5)
# , для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_p(self):
        return (self.width / 6.5 + 0.5)

    def get_c(self):
        return (self.height * 2 + 0.3)

    @property
    def get_full(self):
        return (f'Общая площадь используемой ткани равна {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.full_jacket = (self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.full_jacket}'


a = Jacket(15, 11)
print(a)


class Suit(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.full_suit = (self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на Костюм {self.full_suit}'

b =Suit(15,11)
print(b)
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'{self.title} Запуск отрисовки')


class Pen(Stationery):
    def __init__(title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(title):
        super().__init__(title)
    def draw(self):
        return f'Запуск отрисовки Карандашом'

class Handle(Stationery):
    def __init__(title):
        super().__init__(title)
    def draw(self):
        return f'Запуск отрисовки маркером'

pen = Pen()
pencil = Pencil()
handle = Handle()
a = Stationery('')
a.draw()
pen.draw()
print(pencil.draw())
print(handle.draw())


#
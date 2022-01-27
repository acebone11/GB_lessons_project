# .Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return (f'{self.name} is stopped')

    def turn_left(self):
        return (f'{self.name} turn left')

    def turn_right(self):
        return (f'{self.name} turn right')

    def show_speed(self):
        return (f'Текущая скорость машины {self.speed}')
    def police(self):
        if self.is_police == True:
            return f'{self.name} Это полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.speed} недопустима для городской машины снизьте скорость')
        else:
            print(f'Скорость машины равна {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >40 :
            return f'Слишком большая скорость'
        return (f'Текущая скорость машины {self.speed}')




class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = WorkCar(40, 'Red', 'Audi', False)

print(audi.turn_right())
print(audi.show_speed())
print(audi.police())
print(audi.stop())
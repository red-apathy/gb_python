"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая сторость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости {self.speed}!')
        else:
            print(f'Текущая скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости {self.speed}!')
        else:
            print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):
    pass


police_car_1 = PoliceCar(65, 'Белая', 'Lada', True)
sport_cat_1 = SportCar(120, 'Красная', 'Porsche', False)
town_car_1 = TownCar(55, 'Синяя', 'Honda', False)
work_car_1 = WorkCar(38, 'Желтая', 'Соболь', False)

cars = [police_car_1, sport_cat_1, town_car_1, work_car_1]

for i in cars:
    print(i.color)
    print(i.name)
    print(i.is_police)
    i.go()
    print(i.speed)
    i.show_speed()

    if i == town_car_1:
        i.speed = 61
        print(i.speed)
        i.show_speed()
        i.speed = 59
        print(i.speed)
        i.show_speed()

    elif i == work_car_1:
        i.speed = 41
        print(i.speed)
        i.show_speed()
        i.speed = 39
        print(i.speed)
        i.show_speed()

    i.turn('направо')
    i.stop()
    print('----------------')

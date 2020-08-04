# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 4))


    def running(self):
        for color, sec in cycle(self.__color):
            print(color, 'next color in {} sec'.format(sec))
            sleep(sec)

start = TrafficLight()
start.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self):
        mass = self._lenght * self._width * 25 * 5 / 1000
        print(mass)

road_1 = Road(20, 5000)
road_1.mass()


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


Mike = Position('Mike', 'Smith', 'director', 100000, 50000)
Mike.get_full_name()
Mike.get_total_income()




# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn_left(self):
        print(f'{self.name} повернула налево')
    def turn_right(self):
        print(f'{self.name} повернула направо')
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name}, вы превысили скорость!')
        else:
            print(f'{self.name}, вы едете с допустимой скоростью')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.name}, вы превысили скорость!')
        else:
            print(f'{self.name}, вы едете с допустимой скоростью')

class PoliceCar(Car):
    pass

town_car = TownCar(70,'Синяя', 'Nissan', False)
sport_car = SportCar(240,'Красная', 'Ferrari', False)
work_car = WorkCar(35,'Белая', 'Skoda', False)
police_car = PoliceCar(90,'Белая', 'Ford', True)

town_car.show_speed()
sport_car.go()
sport_car.show_speed()
work_car.show_speed()
work_car.turn_right()
police_car.show_speed()
police_car.stop()


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')

pencil = Pencil('Карандаш')
pencil.draw()
pen = Pen('Ручка')
pen.draw()
handle = Handle('Маркер')
handle.draw()
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for num in day_month_year.split():
            if num != '-': date.append(num)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return f'Корректные данные'
                else:
                    return f'Некорректно введен год'
            else:
                return f'Некорректно введен месяц'
        else:
            return f'некорректно введено число месяца'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'



print(Data('13 - 8 - 2020'))
print(Data.valid(33, 8, 2020))
print(Data.valid(13, 18, 2020))
print(Data.valid(13, 8, 20200))
print(Data.valid(13, 8, 2020))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Divizion_by_Zero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return f'Ошибка: деление на ноль!'


print(Divizion_by_Zero.divide_by_zero(5,6))
print(Divizion_by_Zero.divide_by_zero(5,0))



# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного
# элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class Check_number:
    def __init__(self, *args):
        self.new_list = []

    def my_input(self):

        while True:
            try:
                inputs = int(input('Введите числовое значение: '))
                self.new_list.append(inputs)
                print(f'Список числовых значений: {self.new_list} \n')

            except:
                print('Введенное значение не является числовым')
                cont = input(f'Ввести еще значения или выйти? Y/N ')

                if cont == 'Y' or cont == 'y':
                    continue
                    print(prosess.my_input())
                elif cont == 'N' or cont == 'n':
                    print(self.new_list)
                    break

                else:
                    print(self.new_list)
                    break


prosess = Check_number(56)
print(prosess.my_input())


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Store:
    def __init__(self, name, quantity, price, *args):
        self.name = name
        self.quantity = quantity
        self.price = price

class Printer(Store):
    def to_print(self):
        return f'Принтер печатает'

class Scaner(Store):
    def scan(self):
        return f'Сканер сканирует'
class Xerox(Store):
    def copy(self):
        return f'Ксерокс копирует'

print(Printer.to_print(3))
print(Scaner.scan(3))
print(Xerox.copy(3))

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

class Store:
    def __init__(self, name, quantity, price, *args):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.my_store = []
        self.model = {'Модель устройства': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Модель устройства: {self.name} Цена: {self.price} Количество: {self.quantity}'

    def bring(self):
        model = input('Введите модель устройства: ')
        model_price = input('Введите цену устройства: ')
        model_quantity = input('Введите количество устройств: ')
        result = {'Модель устройства': model, 'Цена': model_price, 'Количество': model_quantity}
        self.model.update(result)
        self.my_store.append(self.model)
        print(f'Оборудование на складе: {self.my_store}')

class Printer(Store):
    def to_print(self):
        return f'Принтер печатает'

class Scaner(Store):
    def scan(self):
        return f'Сканер сканирует'
class Xerox(Store):
    def copy(self):
        return f'Ксерокс копирует'

print(Printer.to_print(3))
print(Scaner.scan(3))
print(Xerox.copy(3))
model_1 = Printer('Canon', 5, 6000)
model_2= Scaner('Canon', 3, 7000)
model_3= Xerox('Xerox', 5, 16000)
print(model_1.bring())

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
class Store:
    def __init__(self, name, quantity, price, *args):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.my_store = []
        self.model = {'Модель устройства': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Модель устройства: {self.name} Цена: {self.price} Количество: {self.quantity}'


    def bring(self):
        try:
            model = input('Введите модель устройства: ')
            model_price = int(input('Введите цену устройства: '))
            model_quantity = int(input('Введите количество устройств: '))
            result = {'Модель устройства': model, 'Цена': model_price, 'Количество': model_quantity}
            self.model.update(result)
            self.my_store.append(self.model)
            print(f'Оборудование на складе: {self.my_store}')
        except:
            return f'Данные введены некорректно'

class Printer(Store):
    def to_print(self):
        return f'Принтер печатает'

class Scaner(Store):
    def scan(self):
        return f'Сканер сканирует'
class Xerox(Store):
    def copy(self):
        return f'Ксерокс копирует'

print(Printer.to_print(3))
print(Scaner.scan(3))
print(Xerox.copy(3))
model_1 = Printer('Canon', 5, 6000)
model_2= Scaner('Canon', 3, 7000)
model_3= Xerox('Xerox', 5, 16000)
print(model_1.bring())

# # 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'

c_1 = Complex_number(5, 6)
c_2 = Complex_number(-4, 8)
print(c_1 + c_2)
print(c_1 * c_2)


















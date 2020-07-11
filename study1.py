#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
a = 5
b = 'key'
c = 6.88
print(a, type(a))
print(b, type(b))
print(c, type(c))
a = int(input())
b = str(input())
c = float(input())
print(a)
print(b)
print(c)

#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
inp_sec = int(input())
whole_sec = inp_sec % 86400
h = int(whole_sec / 3600)
minutes = int(whole_sec / 60 % 60)
sec = int(whole_sec % 60)
print("{:02}:{:02}:{:02}".format(h,minutes,sec))

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input())
print(n+int(str(n)+str(n))+int(str(n)+str(n)+str(n)))

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input())
maximum = number % 10
number = number // 10
while number > 0:
    if number % 10 > maximum:
        maximum = number % 10
    number = number // 10
print(maximum)

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print('Введите сумму выручки')
revenue = float(input())
print('Введите сумму издержек')
costs = float(input())
if revenue > costs:
    print('Ваша фирма работает с прибылью')
    print('Ваша рентабельность:', (revenue-costs)/revenue*100, '%')
    print('Укажите численность сотрудников фирмы')
    n = int(input())
    print('Прибыль фирмы в расчете на одного сотрудника', (revenue-costs)/n, 'рублей')
else:
    print('Ваша фирма работает с убытками')

#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
days = 1
a = float(input())
b = float(input())
while a < b:
    a *= 1.1
    days +=1
print(days)
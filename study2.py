#1.Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
a = [1, 10, 'cow', 7, 'sheep', 5.8, [3, 6], {"kate": 6}]
for el in a:
    print(type(el))
#2.Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
n=0
a = []
a = input().split()
while (len(a) - n) > 1:
    a[n], a[n+1] = a[n+1], a[n]
    n+=2
print(a)
#3.Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
seasons = {'1':'зима', '2':'зима', '12':'зима', '3':'весна', '4':'весна', '5':'весна', '6':'лето', '7':'лето', '8':'лето', '9':'осень', '10':'осень', '11':'осень'}
print('Введите номер месяца:')
month = input()
print('Указанный месяц относится к сезону: ', seasons[month])

seasons = ['none', 'зима', 'зима', 'весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
print('Введите номер месяца:')
month = int(input())
print('Указанный месяц относится к сезону: ', seasons[month])

#4.Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
a = []
a = input().split()
for ind, el in enumerate(a, 1):
    print(ind, el[0:10])
#5.Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
new = int(input())
my_list.append(new)
my_list.sort(reverse=True)
print(my_list)

#6.Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

goods = []
name_list = list(set([]))
price_list = list(set([]))
count_list = list(set([]))
unit_list = list(set([]))

while True:
    name = input("Введите название товара: ")
    price = int(input('Введите стоимость товара: '))
    count = int(input('Введите количество товаров: '))
    unit_measure = input('Введите единицу измерения: ')

    goods.append({
        "название": name,
        "цена":price,
        "количество":count,
        "ед":unit_measure
    })

    name_list.append(name)
    price_list.append(price)
    count_list.append(count)
    unit_list.append(unit_measure)

    analitycs = {
        "название": name_list,
        "цена": price_list,
        "количество": count_list,
        "eд": unit_list
    }


    cont = input("Want to add another? (Y/N)")
    if cont == "N":
        break;

for i in enumerate(goods, 1):
    print(i)

for key,value in analitycs.items():
    print(key, value)
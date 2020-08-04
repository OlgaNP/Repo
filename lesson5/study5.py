# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
data = open("51.txt", "w")
while True:
    text = input()
    if text == '':
        break
    data.write(text + "\n")

data.close()


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
line = 0

for strings in open("5_2.txt"):
    line += 1

    flag = 'out'
    word = 0
    for words in strings:
        if words != " " and flag == 'out':
            word += 1
            flag = 'in'
        elif words == ' ':
            flag = 'out'
    print("Количество слов в строке:", word)


print("Количество строк:", line)

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open("53.txt", encoding ="utf-8") as f:
    salary = []
    low_salary = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            low_salary.append(i[0])
        salary.append(i[1])
print(f'Оклад менее 20000 у: {low_salary}, средний оклад: {sum(map(int,salary))/len(salary)}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
rus_dict = {'One': 'Один','Two': 'Два','Three': 'Три','Four': 'Четыре'}
new = []
with open("54.txt", encoding ="utf-8") as f:
    for i in f:
        i = i.split(' ', 1)
        new.append(rus_dict[i[0]] + i[1])
    print(new)
with open("54_new.txt", "w", encoding ="utf-8", ) as f_2:
    f_2.writelines(new)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open ('55.txt', 'w', encoding='UTF-8') as f:
    numbers = input('Введите числа:')
    f.write('Числа:' + numbers + '\n')
    numbers = map(int, numbers.split())
    sum_numbers = sum(numbers)
    f.write('Сумма:' + str(sum_numbers))

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
lessons = {}
with open('56.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split()
        print(data)
        lesson = data[0]
        number_of_lessons = sum([int(x[:x.find('(')]) for x in data[1:] if '(' in x])
        lessons[lesson] = number_of_lessons
print(lessons)


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

import json
data = {}
median_profit = []

with open('57.txt') as f:
    lines = f.readlines()
    for line in lines:
        name, firm_type, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        data[name] = profit
        if profit > 0:
            median_profit.append(profit)
median_profit = sum(median_profit) / len(median_profit)
info = [data, {'average_profit':median_profit}]

with open('57.json', 'w') as f_json:
    json.dump(info, f_json)

with open('57.json') as f_json:
    print(json.load(f_json))

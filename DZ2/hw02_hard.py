# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.



def Equation(equation, x):
    list_equation = equation.split()
    if list_equation[2][-1] != 'x':
        return False
    else:
        try:
            k = float(list_equation[2][:-1])
        except:
            return False
    if list_equation[3] == '+':
        try:
            b = float(list_equation[4])
        except:
            return False
    elif list_equation[3] == '-':
        try:
            b = -float(list_equation[4])
        except:
            return False
    try:
        y = k * x + b
    except:
        return False
    return y


# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
from datetime import datetime

def checkdate(str_date):
    return_flag = True
    try:
        dt = datetime.strptime(str_date, '%d.%m.%Y')
    except:
        return_flag = False
    list_date = str_date.split('.')
    if(len(list_date[0]) != 2):
        return_flag = False
    if(len(list_date[1]) != 2):
        return_flag = False
    return return_flag
# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

def InvTower(room):
    count_room_floor = 0            # кол-во комнат на этаже
    last_room_floor = 0             # номер последней комнаты
    floor = 0                       # последний этаж предыдущей группы
    while last_room_floor < room:
        floor += count_room_floor
        count_room_floor += 1
        prev_last_room_floor = last_room_floor  # предыдущий последний номер комнаты
        last_room_floor += count_room_floor**2
    return [count_room_floor + (room - prev_last_room_floor - 1) // count_room_floor + 1,
     (room - prev_last_room_floor - 1) % count_room_floor + 1]

def main():
    print('***1***')
    equation = 'y = -12x + 11111140.2121'
    x = 3.4
    print(equation, '\nx = ',x, '\ny = ', Equation(equation,x))
    print('***2***')
    date = ['01.11.1985', '01.22.1001', '1.12.1001', '-2.10.3001',
        '01.01.9999', '31.01.0001']
    for i in date:
        print('{:<10}'.format(i) + ' ->\t', checkdate(i))
    print('***3***')
    print(InvTower(13))
    print(InvTower(11))
    

if __name__ == '__main__':
    main()
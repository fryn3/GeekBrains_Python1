# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
# -1 1/3 + 17/42 - -2 3/14
def my_calc(st):
    _int1 = 0
    _num1 = 0   # числитель
    _denom1 = 1 # знаменатель
    _int2 = 0
    _num2 = 0   # числитель
    _denom2 = 1 # знаменатель
    status = 0
    it = st.split()
    for i, p in enumerate(it):
        if status == 0:
            if p.isdigit() or (p[0] == '-' and p[1:].isdigit()):
                _int1 = int(p)
                status = 1
            elif len(p.split('/')) == 2:
                _num1 = int(p.split('/')[0])
                _denom1 = int(p.split('/')[1])
                status = 2
            else:
                print('not found first number')
                return float('inf');
        elif status == 1:
            if len(p.split('/')) == 2:
                _num1 = int(p.split('/')[0])
                _denom1 = int(p.split('/')[1])
                status = 2
            elif  p == '+' or p == '-':
                sign = p
                status = 3
            else:
                print('_int1 - true; sign - false')
                return float('inf');
        elif status == 2:
            if p == '+' or p == '-':
                sign = p
                status = 3
            else:
                print('number1 - true; sign - false')
                return float('inf');
        elif status == 3:
            if p.isdigit() or (p[0] == '-' and p[1:].isdigit()):
                _int2 = int(p)
                status = 4
            elif len(p.split('/')) == 2:
                _num2 = int(p.split('/')[0])
                _denom2 = int(p.split('/')[1])
                status = 5
            else:
                print('not found second number')
                return float('inf');
        elif status == 4 and len(p.split('/')) == 2:
            _num2 = int(p.split('/')[0])
            _denom2 = int(p.split('/')[1])
            status = 5
        else:
            print('status = ' + str(status) + '\t error in end string')

    ab_denom = _denom1 * _denom2
    if _int1 > 0:
        a_num = _int1 * ab_denom + _num1 * _denom2
    else:
        a_num = _int1 * ab_denom - _num1 * _denom2
    if _int2 > 0:
        b_num = _int2 * ab_denom + _num2 * _denom1
    else:
        b_num = _int2 * ab_denom - _num2 * _denom1

    ab_num = a_num + b_num if sign == '+' else a_num - b_num
    if abs(ab_num) > ab_denom and ab_num > 0:
        res_int = ab_num // ab_denom
        res_num = ab_num % ab_denom
    else:
        res_int = -(abs(ab_num) // ab_denom)
        res_num = abs(ab_num) % ab_denom
    res_denom = ab_denom
    _del = res_num
    while _del > 0:
        if res_num % _del == 0 and res_denom % _del == 0:
            res_num /= _del
            res_denom /= _del
        _del-=1
    if res_num == 0:
        return str(res_int)
    return '{} {}/{}'.format(res_int, int(res_num), int(res_denom))

# ASK: почему от отрицательных чисел деление на цело не правильно(для меня) работают -273//18?
print('***1***')
exm = ['5/6 + 4/7', '-2/3 - -2', '-12 2/6 + -2 1/3', '1 - 1',
        '1/2 + -1/2']
for a in exm:
    print(a + '\t=\t' + my_calc(a))
    print('***********************')


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# 2017.03.08 00:54:34 checked. P.Rusanov
# Отлично!
# Хорошо бы еще ширину выравнивания привязать к максимальной длине строки
print('**1**')
fruct = ["яблоко", "банан", "киви", "арбуз"]
for i, f in enumerate(fruct, 1):
    print('{}.{:>10}'.format(i, f))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# 2017.03.08 00:55:12 checked. P.Rusanov
# Отлично!
print('**2**')
a_list = list(range(10))
b_list = list(range(0, 10, 3))
print(a_list)
print(b_list)
for b_item in b_list:
    while b_item in a_list:
        a_list.remove(b_item)
print(a_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# 2017.03.08 00:55:27 checked. P.Rusanov
# Отлично!
import random
print('**3**')
rand_list = [random.randint(0, 10) for i in range(20)]
print(rand_list)
for index, item in enumerate(rand_list):
    if item % 2:    # не четный
        rand_list[index] *= 2
    else:
        rand_list[index] /= 4
print(rand_list)
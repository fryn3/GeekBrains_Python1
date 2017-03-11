# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# 2017.03.11 13:47:00 checked. P.Rusanov
# Отлично!
def fibonacci(n, m):
    a = [1, 1]
    i = 2
    while i < m - 1:        # Цикл for?
        a.append(a[-1]+a[-2])
        i += 1
    return a[n - 1:]
print('***1***')
print(fibonacci(1,5))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# 2017.03.11 13:47:20 checked. P.Rusanov
# Отлично!
print('***2***')
def sort_to_max(origin_list):
    result = []
    for cycle in range(len(origin_list)):
        _min = origin_list[0]
        for value in origin_list:
            if value < _min:
                _min = value
        result.append(_min)
        origin_list.remove(_min)
    return result

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# 2017.03.11 13:47:44 checked. P.Rusanov
# Отлично! Только немного усложнено...
# Можно ведь просто итерироваться по _array и проверять результат _func(item)
print('***3***')
def my_filter(_func, _array):
    result = []
    for _index, _bool in enumerate(map(_func, _array)):
        if _bool:
            result.append(_array[_index])
    return iter(result)

a = [1, -4, 6, 8, -10]

def func(x):
    if x > 0:        # Сразу return x > 0
            return 1
    else:
            return 0

b = filter(func, a)
my_b = my_filter(func, a)
print(b)
print(my_b)
print(list(b))
print(list(my_b))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# 2017.03.11 13:49:41 checked. P.Rusanov
# Отлично!
print('***4***')

def my_subtraction(x, y):
    return list(map(lambda a, b: a - b, x, y))


def my_pow2(x):
    return list(map(lambda a: a ** 2, x))


# 2017.03.11 13:50:00 checked. P.Rusanov
# Отлично! Также обратите внимание на функцию math.hypot()
def is_parallelogram(a, b, c, d):
    '''Определяет является ли параллелограмм по св-ву:
    Сумма квадратов диагоналей параллелограмма равна сумме квадратов его сторон'''
    return (sum(my_pow2(my_subtraction(a, c))) + sum(my_pow2(my_subtraction(b, d))) ==
        (sum(my_pow2(my_subtraction(a, b))) + sum(my_pow2(my_subtraction(b, c))) + 
            sum(my_pow2(my_subtraction(c, d))) + sum(my_pow2(my_subtraction(a, d)))))

a = [0, 0]
b = [1, 2]
c = [4, 2]
d = [3, 0]
print(is_parallelogram(a, b, c, d))
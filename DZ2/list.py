#!/usr/bin/python3
# coding: utf-8

# Списки

# Заполните код приведённых ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Начало и конец совпадают
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть количество строк,
# длина которых составляет 2 символа и более, 
# а первый и последний символы этих строк совпадают.
# Примечание: в python нет оператора ++. Но += сработает.

# 2017.03.08 01:12:20 checked. P.Rusanov
# Отлично!
def match_ends(words):
    # if type(words) == list:     # Обратите внимание, как PEP8 рекомендует проверять тип объекта
    if isinstance(li, list)
        count = 0
        for word in words:
            if type(word) == str and len(word) > 1:
                if word.endswith(word[0]):
                    count += 1
        return count
    else:
        print('No list')
        return -1


# B. Начинающиеся с X в начале
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть отсортированный список строк, в котором:
# сначала идет группа строк, начинающихся на 'x', затем все остальные.
# Наример: из ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] получится
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Подсказка: это можно сделать при помощи склеивания 2х заранее отсортированных списков

# 2017.03.08 01:13:12 checked. P.Rusanov
# Отлично!
def front_x(words):
    x_list = []
    abc_list = []
    if type(words) == list:
        for index, word in enumerate(words):
            if type(word) == str:
                if len(word) > 0 and word[0] == 'x':
                    x_list.append(word)
                else:
                    abc_list.append(word)
            else:
                print('Var of index = {} is not str'.format(index))
                return -1
        result_list = sorted(x_list)
        result_list.extend(sorted(abc_list))
        return result_list
# Вопрос: почему так не работает?   return sorted(x_list).extend(sorted(abc_list))

# 2017.03.08 01:37:13 checked. P.Rusanov
# Спасибо за интересный вопрос - беру себе в копилку ;)
# .extend() - метод, изменяющий исходный объект, но он возвращает None.
# Хотя объект реально и создается (и наверно даже меняется)
# в return передаётся результат работы метода, а он - None

    else:
        print('No list')
        return -1

# C. Сортировка по последнему числу
# Дан список непустых списков. 
# Нужно вернуть список, отсортированный по 
# возрастанию последнего элемента каждого подсписка.
# Например: из [[1, 7], [1, 3], [3, 4, 5], [2, 2]] получится
# [[2, 2], [1, 3], [3, 4, 5], [1, 7]]
# Подсказка: используйте параметр key= функции сортировки, 
# чтобы получить последний элемент подсписка.

# https://habrahabr.ru/post/138535/

# 2017.03.08 01:39:39 checked. P.Rusanov
# Отлично! Надеюсь, Вы разобрались.
def sortByLastElement(input):
    return input[-1]

def sort_last(lists):
    lists.sort(key = sortByLastElement)
    return lists



# D. Удаление соседей
# Дан список чисел.
# Нужно вернуть список, где все соседние элементы
# были бы сведены к одному элементу.
# Таким образом, из [1, 2, 2, 3, 4, 4] получится [1, 2, 3, 4].

 # 2017.03.08 01:39:58 checked. P.Rusanov
 # Отлично! Попробуйте обойтись без индексов - используйте переменную,
 # хранящую предыдущее значение для каждого шага цикла 
def remove_adjacent(nums):
    for index, a in enumerate(nums):
        while index < len(nums) - 1 and a == nums[index + 1]:
            del nums[index + 1]
    return nums



# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает функции выше с тестовыми параметрами.
def main():
    print('Начало и конец совпадают')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('Начинающиеся с X в начале')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('Сортировка по последнему числу')
    test(sort_last([[1, 3], [3, 2], [2, 1]]),
       [[2, 1], [3, 2], [1, 3]])
    test(sort_last([[2, 3], [1, 2], [3, 1]]),
       [[3, 1], [1, 2], [2, 3]])
    test(sort_last([[1, 7], [1, 6], [3, 4, 5], [2, 2]]),
       [[2, 2], [3, 4, 5], [1, 6], [1, 7]])

    print()
    print('Удаление соседей')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3, 3]), [2, 3])
    test(remove_adjacent([4, 5, 5, 4, 4]), [4, 5, 4])
    test(remove_adjacent([]), [])


if __name__ == '__main__':
    main()


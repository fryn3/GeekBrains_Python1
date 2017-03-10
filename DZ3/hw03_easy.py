# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print('***1***')
def my_round(number, ndigits = 0):
    '''my_round(number[, ndigits]) -> number
    
    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.'''
    st = str(number).split('.')
    if len(st[1]) <= ndigits:
        return number
    if int(st[1][ndigits:]) > 5 * 10 ** (len(st[1][ndigits:]) - 1):
        return int(number * 10 ** ndigits + 1) / 10 ** ndigits
    else:
        return int(number * 10 ** ndigits) / 10 ** ndigits

i_number = 2.1234567
for i in range(10):
    print(str(i) + '\t' + str(my_round(i_number, i)) + '\t' + str(round(i_number, i)))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print('***2***')
def lucky_ticket(ticket_number):
    return True if (sum(map(int, str(ticket_number)[:len(str(ticket_number))//2]))
        == sum(map(int, str(ticket_number)[len(str(ticket_number))//2:]))) else False

print (lucky_ticket(123321))
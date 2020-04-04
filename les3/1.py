"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""

num1 = int(input('Введите делимое число: '))
num2 = int(input('Введите делитель: '))


def my_func(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return 'Делить на 0 нельзя'


print(my_func(num1, num2))

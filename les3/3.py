"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""

number_1 = 100
number_2 = 102
number_3 = 105


def my_func(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 - min(num_1, num_2, num_3)  # не вижу противоречий с заданием


print(my_func(number_1, number_2, number_3))

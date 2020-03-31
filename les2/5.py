"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

print(f'Изначальный список: {my_list}')

new_number = int(input('Введите новое число: '))

last_number = None  # индекс последнего элемента с таким же значением, как и введенное число пользователя

for i in range(len(my_list)):
    if my_list[i] == new_number:
        last_number = i

try:
    my_list.insert(last_number + 1, new_number)
except TypeError:
    my_list.append(new_number)
    my_list.sort(reverse=True)

print(f'Список с добавленным пользователем числом {new_number}: {my_list}')
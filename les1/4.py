"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while
и арифметические операции.
"""

number = input('Введите число: ')

max_number = 0

for i in number:
    while int(i) > max_number:
        max_number = int(i)
print(max_number)

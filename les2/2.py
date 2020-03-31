"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
использовать функцию input().
"""

pre_list = []

len_list = int(input('Введите длину для вашего списка: '))

for element in range(len_list):
    pre_list.append(input(f'Введите {element} элемент для добавления в ваш список: '))

print(f'Это ваш составленный список: {pre_list}')

operation_list = []

first_el = 0
second_el = 2

while True:
    rev = pre_list[first_el:second_el]
    if len(rev) == 2:
        operation_list.append(rev[::-1])
    elif len(rev) == 1:
        operation_list.append(rev)
    else:
        break
    first_el += 2
    second_el += 2

user_list = []

for i in operation_list:
    for j in i:
        user_list.append(j)

print(f'Это ваш список с переставленными соседними элементами: {user_list}')

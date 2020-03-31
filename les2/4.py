"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_str = input('Введите через пробел несколько слов: ')

operation_list = []

for i in user_str.split():
    operation_list.append(i)

for i in range(len(operation_list)):
    print(i + 1, operation_list[i][0:10])

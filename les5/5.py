"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('quest5.txt', 'w') as f_obj:
    f_obj.write(input('Введите числа через пробел: '))

with open('quest5.txt', 'r') as f_obj:
    try:
        print(sum(map(int, f_obj.readline().split())))
    except ValueError:
        print('В файл ввели текстовые знаки')

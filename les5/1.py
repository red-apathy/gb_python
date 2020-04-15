"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

file_obj = open('quest1.txt', 'w', encoding='utf-8')

write_line = None
while True:
    write_line = input('Введите текст (чтобы прекратить ввод - не заполняя строку ввода нажмите "ENTER"): ')
    if write_line == '':
        file_obj.close()
        break
    else:
        file_obj.write(write_line + '\n')

with open("quest1.txt", "r", encoding='utf-8') as file_obj:
    print(file_obj.read())

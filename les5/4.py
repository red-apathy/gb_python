"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

translate = {'One': 'Один',
             'Two': 'Два',
             'Three': 'Три',
             'Four': 'Четыре'}

with open('quest4.txt', 'r', encoding='utf-8') as first_f_obj:
    new_lines = []
    for line in first_f_obj:
        if line != '':
            new_lines.append(line.replace(line.split(' — ')[0], translate[line.split(' — ')[0]]))

with open('quest4-2.txt', 'w', encoding='utf-8') as second_f_obj:
    for i in new_lines:
        second_f_obj.write(i)

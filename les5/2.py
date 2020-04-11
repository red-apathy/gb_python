"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('quest2.txt', 'r', encoding='utf8') as file_obj:
    lines = file_obj.readlines()

print(f'Количество строк в файле: {len(lines)}')

for line_num in range(len(lines)):
    print(f'Строка №{line_num} имеет {len(lines[line_num].split())} слов')

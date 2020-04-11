"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

with open('quest7.txt', 'r', encoding='utf-8') as f_obj:
    firms = []
    firm_indicators = {}
    for line in f_obj:
        firm_indicators.update(
            {f'{line.split()[1]} {line.split()[0]}': f'{int(line.split()[2]) - int(line.split()[3])}'})

average_profit = 0
q = 0
for profit in list(firm_indicators.values()):
    if int(profit) > 0:
        average_profit += int(profit)
        q += 1
    else:
        pass
average_profit /= q

firms.append(firm_indicators)
firms.append({'average_profit': f'{average_profit}'})

with open('quest6.json', 'w', encoding='utf8') as write_json:
    json.dump(firms, write_json)

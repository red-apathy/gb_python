"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, hours, rate, prize = argv


def salary(hours_arg, rate_srg, prize_srg):
    return int(hours_arg) * int(rate_srg) + int(prize_srg)


print(salary(hours, rate, prize))

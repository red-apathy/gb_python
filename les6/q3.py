"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income
доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, vage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'vage': vage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return sum(list(self._income.values()))


worker_1 = Position('Иван', 'Иванов', 'Токарь', 45000, 10000)
print(worker_1.name, worker_1.surname, worker_1.position, worker_1._income)
print(worker_1.get_full_name())
print(worker_1.get_total_income())

worker_2 = Position('Сергей', 'Сергеев', 'Сварщик', 55000, 15000)
print(worker_2.name, worker_2.surname, worker_2.position, worker_2._income)
print(worker_2.get_full_name())
print(worker_2.get_total_income())

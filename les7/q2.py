"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Garment(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Garment):
    def __init__(self, v):
        self._v = v

    @property
    def check_v(self):
        if self._v > 0:
            return self._v
        else:
            raise ValueError

    def consumption(self):
        return self._v / 6.5 + 0.5


class Costume(Garment):
    def __init__(self, h):
        self._h = h

    @property
    def check_h(self):
        if self._h > 0:
            return self._h
        else:
            raise ValueError

    def consumption(self):
        return 2 * self._h + 0.3


my_coat = Coat(52)
print(my_coat.check_v)
print(my_coat.consumption())

my_costume = Costume(180)
print(my_costume.check_h)
print(my_costume.consumption())

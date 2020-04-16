"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


base_class_obj = Stationery('Кисть')
base_class_obj.draw()

pen_obj = Pen('Простой')
pen_obj.draw()

pencil_obj = Pencil('Шариковая')
pencil_obj.draw()

handle_obj = Handle('Спиртовой')
handle_obj.draw()

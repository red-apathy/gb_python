"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix = ''
        for i in self.matrix_list:
            line = ''
            for j in i:
                line += str(j)
                if j != i[-1]:
                    line += ' '
            if i != self.matrix_list[-1]:
                line += '\n'
            matrix += line
        return matrix

    def __add__(self, other):
        new_matrix = []
        if len(self.matrix_list) != len(other.matrix_list):
            raise ValueError
        for line in range(len(self.matrix_list)):
            new_line = []
            if len(self.matrix_list[line]) != len(other.matrix_list[line]):
                raise ValueError
            for iter_el in range(len(self.matrix_list[line])):
                new_line.append(self.matrix_list[line][iter_el] + other.matrix_list[line][iter_el])
            new_matrix.append(new_line)
        return new_matrix


mx1 = Matrix([[1, 2, 3, 6], [4, 5, 6, 7]])
mx2 = Matrix([[1, 2, 3, 8], [4, 5, 6, 10]])
mx3 = Matrix(mx1 + mx2)
print(mx3)

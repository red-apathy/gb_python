"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Game:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.barrel_list = None
        self.barrel = None

    def get_barrel(self):
        """Генерация бочонка из мешка"""
        self.barrel = str(random.choice(self.barrel_list))
        self.barrel_list.remove(int(self.barrel))
        print(f'Новый бочонок: {self.barrel} (осталось {len(self.barrel_list)})')

    def make_barrel_list(self):
        """Составление мешка с бочонками"""
        self.barrel_list = list(range(1, 91))

    def player_turn(self):
        """Ход игрока"""
        while True:
            action = input('Зачеркнуть цифру? (y/n) ')
            if action == 'y' or action == 'n':
                break
            continue

        if action == 'n':
            if f' {self.barrel} ' in self.player.card:
                return 'lose'
        elif action == 'y':
            if f' {self.barrel} ' in self.player.card:
                self.change_barrel(player)
            else:
                return 'lose'

    def computer_turn(self):
        """Ход компьютера"""
        if f' {self.barrel} ' in self.computer.card:
            self.change_barrel(computer)
        else:
            pass

    def change_barrel(self, player_obj):
        if len(self.barrel) == 2:
            player_obj.card = player_obj.card.replace(f' {self.barrel} ', '  X ')
        else:
            player_obj.card = player_obj.card.replace(f' {self.barrel} ', ' X ')

    @classmethod
    def check_win(cls):
        """Проверка победы"""
        if player.card.count('X') == 15 and computer.card.count('X') == 15:
            print('Ничья!')
        elif player.card.count('X') == 15:
            print(f'Победил {player.name}')
        elif computer.card.count('X') == 15:
            print(f'Победил {computer.name}')
        else:
            return 'next'

    def start(self):
        """Запускатор"""
        while True:
            ans = input('Хотите сыграть в лото? (y/n) ')
            if ans == 'y':
                player.create()
                computer.create()
                self.make_barrel_list()
            elif ans == 'n':
                break
            else:
                continue
            while True:
                self.get_barrel()
                computer.show_card()
                player.show_card()
                if self.player_turn() == 'lose':
                    print('Вы проиграли!')
                    break
                self.computer_turn()
                if self.check_win() is None:
                    computer.show_card()
                    player.show_card()
                    break


class Card:

    def __init__(self, name):
        self.name = name
        self.card = None

    def create(self):
        """
        Генерация карточки по следующий условиям:
        1. 15 цифр на карточке
        2. Каждый десяток цифр распологается в своем столбце
        3. Не более 3 цифр одного десятка в столбце на карточке (как в настоящем лото)
        4. В ряду 5 цифр и 4 пустых ячейки
        5. В 1 столбце не может быть 3 пустых ячейки
        """

        """Формирую 27 цифр"""
        matrix = [[], [], []]
        for i in range(9):
            if i == 0:
                num = random.sample(range(1, 10), 3)
            elif i == 8:
                num = random.sample(range(80, 91), 3)
            else:
                num = random.sample(range(i * 10, i * 10 + 10), 3)
            for j in range(len(num)):
                matrix[j].append(num[j])

        """
        Получаю случайным образом индексы чисел по рядам, в которые надо вставить пробел вместо цифры. Если в столбце
        удаляются все 3 числа, то индексы генерируются заново
        """
        while True:
            martix_del = []
            check = 0
            for line in range(len(matrix)):
                martix_del.append(random.sample(range(0, 9), 4))
            for i in range(4):
                if martix_del[0][i] in martix_del[1] and martix_del[0][i] in martix_del[2]:
                    check = 1
            if check == 1:
                continue
            else:
                break

        """Удаление лишних цифр"""
        for i in range(len(martix_del)):
            for j in martix_del[i]:
                matrix[i][j] = '-'

        """Составление карточки лото"""
        card = f"{self.name}'s card\n"

        for i in matrix:
            for j in i:
                if len(str(j)) == 1:
                    j = f' {j}'
                card += f'{j} '
            card += '\n'
        card += '--------------------------'
        self.card = card

    def show_card(self):
        """Показ карточки игроку"""
        print(f'{self.card}')


player = Card('Player')
computer = Card('Computer')

game = Game(player, computer)
game.start()

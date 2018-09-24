import getopt
import sys

import numpy as np

X = 'x'
Y = 'y'
# 'Шаг' - на сколько ячеек сдвигается указатель за раз.
STEP = 1

# Сообщение с подсказкой. Показывается при запуске с параметром 'help'
HELP_TEXT = 'main.py -n <n> [-s][help]'


def generate_matrix(size):
    """
    Возвращает матрицу size x size, заполненную случайными числами
    из диапазона 0-9999
    """
    return np.random.randint(10000, size=(size, size))


def printout_matrix(matrix):
    """Вывод матрицы на экран"""
    size = len(matrix)
    for i in range(0, size):
        for j in range(0, size):
            # Значения дополняются слева пробелами, чтобы матрица была ровной.
            # 5 - потому что матрица запоняется значениями в диапазоне 0-9999
            print(str(matrix[i][j]).rjust(5, ' '), end='')
        print('\n', end='')
    # flush
    print()


def invert(i):
    return -i


def printout_spiral(n, show_matrix=False):
    """
    Вывод значений матрицы от центра по спирали против часовой стрелки.
    Для матрицы:
    4 5 3 5 3
    7 8 5 6 4
    4 5 2 7 1
    2 5 2 8 9
    4 5 8 6 9
    будет выведена такая строка:
    2 5 5 2 8 7 6 5 8 7 4 2 4 5 8 6 9 9 1 4 3 5 3 5 4

    :param n: определяет размер матрицы 2n-1 x 2n-1
    :param show_matrix: Флаг, указывающий необходимость вывода на экран матрицы
    """
    # размерность матрицы
    size = 2 * n - 1
    # максимальный индекс при обращении к элементам матрицы
    max_index = size - 1

    matrix = generate_matrix(size)
    # текущее положение указателя
    pointer = {X: int(max_index / 2), Y: int(max_index / 2)}

    if show_matrix:
        printout_matrix(matrix)

    # вывод центрального элемента
    print(matrix[pointer[X]][pointer[Y]], end=' ')
    # количество шагов в текущем цикле
    number_of_steps = 1
    # направление шага вдоль оси
    direction = 1
    # пока не достигли верхнего левого элемента матрицы
    while pointer[X] != 0 or pointer[Y] != 0:
        direction = invert(direction)
        # Y - горизонталь, X - вертикаль.
        # Поэтому ключи отсортированы в обратном порядке
        for dimension in sorted(pointer.keys(), reverse=True):
            for _ in range(number_of_steps, 0, -1):
                # сдвиг указателя на один шаг в заданном направлении
                pointer[dimension] += STEP * direction
                print(matrix[pointer[X]][pointer[Y]], end=' ')

            # если достигли верхнего левого элемента матрицы, прерываем цикл
            if pointer[X] == 0 and pointer[Y] == 0:
                break

            direction = invert(direction)
        # количество шагов в цикле ограничено максимально допустимым индексом
        # в матрице
        if number_of_steps < max_index:
            number_of_steps += 1
    # flush
    print()


def main(argv):
    n = None
    show_matrix = False

    try:
        opts, args = getopt.getopt(argv, 'n:s', ['help'])

        if '--help' in args:
            print(HELP_TEXT)
            sys.exit(0)

        for opt in opts:
            if opt[0] == '-n':
                n = opt[1]
            elif opt[0] == '-s':
                show_matrix = True

        if not n:
            print(HELP_TEXT)
            sys.exit(2)

        try:
            n = int(n)
        except ValueError:
            print('n должно быть целым числом')
            sys.exit(2)

        if n <= 0:
            print('n должно быть больше нуля')
            sys.exit(2)

        printout_spiral(n, show_matrix)

    except getopt.GetoptError:
        print(HELP_TEXT)
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])

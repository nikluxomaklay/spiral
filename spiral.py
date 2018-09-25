import argparse

import numpy as np

# Максимальное значение в ячейках матрицы
MATRIX_VALUE_LIMIT = 10000
MATRIX_VALUE_LENGTH = len(str(MATRIX_VALUE_LIMIT))


def check_positive(value):
    """Проверка, что аргумент - положительный int"""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            f"{value} is an invalid positive int value")

    return ivalue


def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '-n',
        type=check_positive,
        help='Определяет размер матрицы 2n-1 x 2n-1',
        action='store'
    )
    arg_parser.add_argument(
        '-s', '--show',
        help='Флаг, указывающий необходимость вывода на экран матрицы',
        action='store_true'
    )

    return arg_parser.parse_args()


def generate_matrix(size, value_limit):
    """
    Возвращает матрицу size x size, заполненную случайными числами
    из диапазона [0..value_limit)
    """
    return np.random.randint(value_limit, size=(size, size))


def printout_matrix(matrix):
    """Вывод матрицы на экран"""
    size = len(matrix)
    max_value_length = len(str(matrix.max()))
    printed_text = '\n'
    for i in range(0, size):
        for j in range(0, size):
            # Значения дополняются слева пробелами, чтобы матрица была ровной.
            printed_text = (
                f'{printed_text}'
                f'{str(matrix[i][j]).rjust(max_value_length + 1, " ")}'
            )
        printed_text = f'{printed_text}\n'

    print(printed_text)
    return printed_text


def invert(i):
    return -i


def printout_spiral(matrix):
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
    """
    printed_text = ''

    # 'Шаг' - на сколько ячеек сдвигается указатель за раз.
    STEP = 1
    X = 'x'
    Y = 'y'
    # максимальный индекс при обращении к элементам матрицы
    max_index = matrix.shape[0] - 1
    # текущее положение указателя
    pointer = {X: int(max_index / 2), Y: int(max_index / 2)}

    # центральный элемент
    printed_text = f'{printed_text}{matrix[pointer[X]][pointer[Y]]} '
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
                printed_text = (
                    f'{printed_text}{matrix[pointer[X]][pointer[Y]]} '
                )

            # если достигли верхнего левого элемента матрицы, прерываем цикл
            if pointer[X] == 0 and pointer[Y] == 0:
                break

            direction = invert(direction)
        # количество шагов в цикле ограничено максимально допустимым индексом
        # в матрице
        if number_of_steps < max_index:
            number_of_steps += 1

    print(printed_text)
    return printed_text


def main(n, value_limit=MATRIX_VALUE_LIMIT, show_matrix=False):
    """
    Генерирует матрицу размером 2n-1 x 2n-1,
    заполненную рандомными значениями в диапазоне [0..value_limit).
    Выводит элементы матрицы по спирали - от центра против часовой стрелки.

    :param n: определяет размер матрицы 2n-1 x 2n-1
    :param value_limit: Максимальное значение элемента матрицы
    :param show_matrix: Флаг, указывающий необходимость вывода на экран матрицы
    """
    # размерность матрицы
    size = 2 * n - 1
    matrix = generate_matrix(size, value_limit)

    if show_matrix:
        printout_matrix(matrix)

    printout_spiral(matrix)


if __name__ == '__main__':
    args = parse_args()
    main(args.n, show_matrix=args.show)

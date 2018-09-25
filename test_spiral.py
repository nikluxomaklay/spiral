import numpy
from spiral import generate_matrix
from spiral import invert
from spiral import MATRIX_VALUE_LIMIT
from spiral import printout_matrix
from spiral import printout_spiral


def test_matrix():
    matrix = generate_matrix(size=5, value_limit=MATRIX_VALUE_LIMIT)

    assert isinstance(matrix, numpy.ndarray)
    assert matrix.shape == (5, 5)
    assert matrix.min() >= 0, matrix.max < MATRIX_VALUE_LIMIT


def test_printout_matrix():
    expected = '\n 0 0 0\n 0 0 0\n 0 0 0\n'
    matrix = generate_matrix(size=3, value_limit=1)
    printed_matrix = printout_matrix(matrix=matrix)

    assert printed_matrix == expected


def test_invert():
    value = 1
    ivalue = invert(value)

    assert value == -ivalue


def test_printout_spiral():
    expected = '5 4 7 8 9 6 3 2 1 '
    matrix = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    printed_text = printout_spiral(matrix)

    assert printed_text == expected

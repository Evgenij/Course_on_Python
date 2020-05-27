import numpy
from numpy.linalg import det, inv


def multimatrix():
    print('multimatrix: ')
    first_matrix = numpy.arange(3 * 5).reshape((3, 5))
    second_matrix = numpy.arange(5 * 2).reshape((5, 2))

    print('First: \n', first_matrix)
    print('Second: \n', second_matrix)
    print('Mult: \n', first_matrix @ second_matrix)
    print()

def multivector():
    print('multivector: ', end='')
    matrix = numpy.arange(2 * 3).reshape((3, 2))
    vector = numpy.array([1, -1], dtype=float)
    print(matrix @ vector)
    print()


def linalg():
    print('linalg: ', end='')
    matrix = numpy.array([[-7., 4.], [6., -8.]])
    vector = numpy.array([2., -9.])
    print(numpy.linalg.solve(matrix, vector))
    print()


def determin():
    print('determin: ', end='')
    matrix = numpy.arange(5 * 5).reshape((5, 5))
    print(det(matrix))
    print()


def invmatrix():
    print('invmatrix: ')
    a = numpy.array([[4, 9, 3], [0, 5, 4], [7, 2, 9]])
    a_invented = inv(a)
    print(a_invented)
    print()


def transmatrix():
    print('transmatrix: ')
    a = numpy.array([[8, 4, 1], [2, 7, 4]])
    a = a.transpose()
    print(a)
    print()



multimatrix()
multivector()
linalg()
determin()
invmatrix()
transmatrix()

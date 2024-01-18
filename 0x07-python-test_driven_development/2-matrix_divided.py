#!/usr/bin/python3
"""Module divides elements of a matrix by an integer"""


def matrix_divided(matrix, div):
    """
    Function divides elements of a matrix by a divisor.

    Args:
        Matrix()
        div(int):

    Returns:
        A new matrix.
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, int):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for m in range(len(matrix)):
        if not isinstance(matrix[m], list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        if len(matrix[0]) != len(matrix[m]):
            raise TypeError('Each row of the matrix must have the same size')
        for n in range(len(matrix[m])):
            if not isinstance(matrix[m][n], (int, float)):
                raise TypeError('matrix must be a \
matrix (list of lists) of integers/floats')
    new_matrix = []
    for rows in range(len(matrix)):
        new_matrix.append([])
        for cols in range(len(matrix[rows])):
            new_matrix[rows].append(float(f'{matrix[rows][cols]/div:.2f}'))

    return new_matrix

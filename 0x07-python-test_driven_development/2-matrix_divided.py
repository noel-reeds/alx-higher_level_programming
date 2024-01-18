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
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for m in range(len(matrix)):
        if not isinstance(matrix[m], list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for n in range(len(matrix[m])):
            if not isinstance(matrix[m][n], (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = []
    for rows in range(len(matrix)):
        new_matrix.append([])
        for cols in range(len(matrix[rows])):
            new_matrix[rows].append(float('{:.2f}'.format(matrix[rows][cols]/div)))

    return new_matrix

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
    new_matrix = []
    for rows in matrix:
        for cols in rows:
            new_matrix.append('{:.2f}'.format(cols/div))
    
    return new_matrix

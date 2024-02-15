#!/usr/bin/python3
"""
Matrix Multiplication Module
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for var in range(len(m_a)):
        if not isinstance(m_a[var], list):
            raise TypeError('m_a must be a list of lists')
        elif len(m_a[var]) == 0:
            raise ValueError("m_a can't be empty")
        for var1 in range(len(m_a[var])):
            if not isinstance(m_a[var][var1], (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(m_a[var]):
            raise TypeError("each row of m_a must be of the same size")
    for var in range(len(m_b)):
        if not isinstance(m_b[var], list):
            raise TypeError('m_b must be a list of lists')
        elif len(m_b[var]) == 0:
            raise ValueError("m_b can't be empty")
        for var2 in range(len(m_b[var])):
            if not isinstance(m_b[var][var2], (float, int)):
                raise TypeError("m_b should contain only integers or floats")
        if len(m_b[0]) != len(m_b[var]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):  # cols of m_a must be eq to rows of m_b
        raise TypeError("m_a and m_b can't be multiplied")

    rows_m_a = len(m_a)
    cols_m_a = len(m_a[0])
    cols_m_b = len(m_b[0])

    # create a res_matrix
    res = [[0 for row in range(cols_m_b)] for col in range(rows_m_a)]

    for var in range(rows_m_a):
        for var1 in range(cols_m_b):
            for var3 in range(cols_m_a):
                res[var][var1] += m_a[var][var3] * m_b[var3][var1]
    return res

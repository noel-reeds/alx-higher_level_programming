#!/usr/bin/python3
"""
Lazy matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):

    m_A = np.matrix(m_a)
    m_B = np.matrix(m_b)

    res = m_A * m_B
    return res

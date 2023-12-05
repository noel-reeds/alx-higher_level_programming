#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return None
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            print("{:d}".format(matrix[m][n]), end=" ")
        print()

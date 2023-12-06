#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for n in m:
            print("{:d}".format(n), end=" ")
        print()

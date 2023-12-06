#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for n in m:
            if n != m[-1]:
                print("{:d}".format(n), end=" ")
            else:
                print("{:d}".format(n), end="")
        print()

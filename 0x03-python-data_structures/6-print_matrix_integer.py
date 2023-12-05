#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            print("{}".format(matrix[m][n]), end=" ")
        print("{}".format("\n")

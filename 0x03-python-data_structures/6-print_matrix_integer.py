#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for x in matrix:
            for y in range(x):
                if y == range(x) - 1:
                    print("{:d}".format(y), end="")
                else:
                    print("{:d}".format(y), end=" ")
            print("")

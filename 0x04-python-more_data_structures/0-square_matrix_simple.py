#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_N = matrix.copy()

    for i in range(len(matrix)):
        matrix_N[i] = list(map(lambda x: x**2, matrix[i]))
    return(matrix_N)

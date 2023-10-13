#!/usr/bin/python3

def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    mxerror = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        new_row = []
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(mxerror)
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix

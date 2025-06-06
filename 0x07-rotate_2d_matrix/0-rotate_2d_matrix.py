#!/usr/bin/python3
"""method that calculates the fewest number
of operations needed to result in exactly n H
"""


def rotate_2d_matrix(matrix):
    """ Transpose the matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

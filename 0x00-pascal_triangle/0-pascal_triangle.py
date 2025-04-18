#!/usr/bin/python3
"""Generate Pascal's Triangle up to the specified number of rows.

This module provides a function to compute Pascal's Triangle, a triangular array
of the binomial coefficients.
"""


def pascal_triangle(n):
    """Generate Pascal's Triangle with n rows.

    Args:
        n (int): Number of rows to generate in the triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
                       Returns a list containing an empty list if n <= 0.

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return [[]]
    tri = [[1]]
    while (n > 1):
        row = []
        for i in range(len(tri[-1])):
            if i == 0:
                row.append(1)
            else:
                row.append(tri[-1][i - 1] + tri[-1][i])
        row.append(1)
        tri.append(row)
        n -= 1
    return tri

#!/usr/bin/env python3
"""Generate Pascal's Triangle up to the specified number of rows.

This module provides a function to compute Pascal's Triangle, a
triangular array of the binomial coefficients.
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
        return []

    triangle = [[1]]  # Initialize with the first row

    while n > 1:
        previous_row = triangle[-1]
        current_row = [1]  # Each row starts with 1

        # Generate middle elements by summing adjacent elements
        for i in range(1, len(previous_row)):
            current_row.append(previous_row[i - 1] + previous_row[i])

        current_row.append(1)  # Each row ends with 1
        triangle.append(current_row)
        n -= 1

    return triangle

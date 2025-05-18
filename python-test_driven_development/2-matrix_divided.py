#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix: list of lists of integers or floats
        div: the number to divide by

    Returns:
        A new matrix with elements divided and rounded to 2 decimal places

    Raises:
        TypeError: if matrix is not a list of lists of numbers,
                   or rows aren't the same size,
                   or div isn't a number
        ZeroDivisionError: if div is 0
    """
    # Matrix type checks
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Row size check
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div checks
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Computation
    return [[round(num / div, 2) for num in row] for row in matrix]

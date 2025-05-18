#!/usr/bin/python3
"""
This module divides all elements of a matrix by a number
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int or float): divisor

    Returns:
        list of lists: new matrix with values rounded to 2 decimal places
    """
    # Check if div is valid
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div != div or div == float('inf') or div == float('-inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix structure
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Perform division
    return [[round(x / div, 2) for x in row] for row in matrix]

#!/usr/bin/python3
"""
This module provides the add_integer function.
It adds two integers or floats (which are cast to integers).
If inputs are not int or float, a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: first number (int or float)
        b: second number (int or float, default 98)

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

#!/usr/bin/python3
"""
Class BaseGeometry with area method and integer validator.
"""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): name of the value.
            value (int): value to validate.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

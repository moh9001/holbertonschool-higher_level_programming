#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle using BaseGeometry integer validation."""

    def __init__(self, width, height):
        """Initializes a rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

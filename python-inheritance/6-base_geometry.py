#!/usr/bin/python3
"""
Class BaseGeometry with an area method that is not implemented.
"""

class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an exception since area is not implemented."""
        raise Exception("area() is not implemented")

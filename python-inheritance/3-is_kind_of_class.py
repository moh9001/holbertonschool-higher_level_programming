#!/usr/bin/python3
"""
Function that checks if an object is an instance of a class or its subclass
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or its subclass"""
    return isinstance(obj, a_class)

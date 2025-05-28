#!/usr/bin/python3
"""
Function that checks if object is an instance of a subclass of a_class
"""

def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class
    (but not an instance of a_class itself)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

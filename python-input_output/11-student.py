#!/usr/bin/python3
"""Defines a Student class with JSON serialization and deserialization."""


class Student:
    """Represents a student with load/save capabilities."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation with optional filtering."""
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                k: getattr(self, k) for k in attrs if hasattr(self, k)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student from dictionary"""
        for key, value in json.items():
            setattr(self, key, value)

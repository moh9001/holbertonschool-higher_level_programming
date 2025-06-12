#!/usr/bin/python3
"""Defines a CustomObject class that can be pickled."""
import pickle


class CustomObject:
    """Custom class with serialization support."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize and save the object to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """Load and return an object from a file, or None on error."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None

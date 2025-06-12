#!/usr/bin/python3
"""Writes text to a file and returns the number of characters written."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

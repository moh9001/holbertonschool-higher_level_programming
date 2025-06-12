#!/usr/bin/python3
"""Appends text to a file and returns the number of characters added."""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file and returns character count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

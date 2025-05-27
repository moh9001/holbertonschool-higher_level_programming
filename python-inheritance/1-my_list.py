#!/usr/bin/python3
"""Module that defines a subclass of list with a sorted print method."""


class MyList(list):
    """A subclass of list that adds a method to print the list sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

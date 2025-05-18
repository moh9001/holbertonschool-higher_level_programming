#!/usr/bin/python3
"""Unittest for max_integer([...])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -10, -3]), -3)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-5, 100, 0, -300]), 100)

    def test_all_same(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.5, 3.9, 2.1]), 3.9)

    def test_strings(self):
        self.assertEqual(max_integer("Holberton"), "t")  # max char

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["Alpha", "Beta", "Zeta"]), "Zeta")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


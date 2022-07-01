#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittest for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 2, 4]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list starting with max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test a list with just one item."""
        single_element = [6]
        self.assertEqual(max_integer(single_element), 6)

    def test_floats(self):
        """Test a list of floats."""
        list_of_floats = [2.53, 16.5, -8.123, 16.0, 7.33]
        self.assertEqual(max_integer(list_of_floats), 16.5)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.55, 2.75, -7, 10, 12]
        self.assertEqual(max_integer(ints_and_floats), 12)

    def test_string(self):
        """Test a string."""
        string = "Richard"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_string(self):
        """Test a list of strings."""
        strings = ["My", "name", "is", "Richard"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): Size of new square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, val):
        """Sets the value of the size."""
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """Returns the current square area."""
        return (self.__size * self__size)

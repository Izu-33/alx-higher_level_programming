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
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self__size)

#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int): Size of new square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) > 2: 
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self__size)

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if size.__self == 0:
            print()
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()


#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

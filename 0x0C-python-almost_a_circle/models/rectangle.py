#!/usr/bin/python3
"""Defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the new rectangle.
            y (int): The y coordinate of the new rectangle.
            id (int): The identity of the rectangle.
        Raises:
            TypeError: If either of the width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """get/set the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """get/set the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """get/set the x coordinate of the rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeErroe("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """get/set the y coordinate of the rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """Returns the area value of the Rectangle instance."""
            return self.__width * self.__height

        def display(self):
            """Prints the Rectangle instance with the character #."""
            if self.__width == 0 or self.__height == 0:
                print("")
                return

            for y in range(self.__y):
                print("")
            for i in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")

        def __str__(self):
            """Return str() representation of the Rectangle."""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                           self.__x,
                                                           self.__y,
                                                           self.__width,
                                                           self.__height)

        def update(self, *args, **kwargs):
            """Update the rectangle.

            Args:
                *args (int): Attribute values.
                **kwargs (dict): key/value pairs of attributes.
            """
            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.__width, self.__height,
                                          self.__x, self.__y)
                        else:
                            self.id = arg
                    elif a == 1:
                        self.__width = arg
                    elif a == 2:
                        self.__height = arg
                    elif a == 3:
                        self.__x = arg
                    elif a == 4:
                        self.__y = arg
                    a += 1
            elif kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(self.__width, self.__height,
                                          self.__x, self.__y)
                        else:
                            self.id = v
                    elif k == "width":
                        self.__width = v
                    elif k == "height":
                        self.__height = v
                    elif k == "x":
                        self.__x = v
                    elif k == "y":
                        self.__y = v

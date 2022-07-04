#!/usr/bin/python3
"""Defines a MyInt class which inherits from int class."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == operator with !=."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with ==."""
        return self.real == value

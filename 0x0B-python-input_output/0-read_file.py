#!/usr/bin/python3
"""Defines a text file reading func."""


def read_file(filename=""):
    """Print the content of a UTF-8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

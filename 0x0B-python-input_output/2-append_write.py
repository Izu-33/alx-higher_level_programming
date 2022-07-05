#!/usr/bin/python3
"""Defines a file append func."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

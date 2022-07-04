#!/usr/bin/python3
"""Defines function to check if an object is an instance of a class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to ckeck.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

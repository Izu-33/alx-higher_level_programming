#!/usr/bin/python3
"""Defines a JSON file-writing func."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))

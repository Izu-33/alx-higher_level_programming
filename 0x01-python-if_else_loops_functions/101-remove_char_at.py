#!/usr/bin/python3
def remove_char_at(str, n):
    """Creats copy of str excluding char at n index."""
    if n >= 0:
        str = str[:n] + str[n + 1:]
    return str

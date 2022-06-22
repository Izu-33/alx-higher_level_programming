#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integer elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        The number of elements printed.
    """
    num = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print()
    return num

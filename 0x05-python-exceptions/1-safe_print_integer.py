#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        print('Handling run-time error:', err)
        return False
    else:
        return True

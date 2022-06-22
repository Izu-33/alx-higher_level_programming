#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end='')
            num += 1
        except (ValueError, TypeError):
            continue
        except IndexError as err:
            print('Handling run-time error:', err)
    print()
    return num

#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for i in my_list[:x]:
        try:
            print(i, end='')
            num += 1
        except IndexError as err:
            print('Handling run-time error:', err)
    print()
    return num

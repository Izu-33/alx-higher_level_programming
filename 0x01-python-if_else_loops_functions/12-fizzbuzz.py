#!/usr/bin/python3
def fizzbuzz():
    """Print numbers 1 to 100.

    Print Fizz in place of number for multiples of 3.
    Print Buzz in place of number for multiples of 5.
    Print FizzBuzz in place of number for multiples of 3 and 5.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")

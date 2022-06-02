#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = 0
    for num in range(len(sys.argv) - 1):
        n += int(sys.argv[num + 1])
    print("{}".format(n))

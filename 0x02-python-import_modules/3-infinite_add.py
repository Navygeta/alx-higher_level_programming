#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    _sum = 0
    for i in range(1, len(sys.argv)):
        _sum += int(sys.argv[i])
    print(f"{_sum}")

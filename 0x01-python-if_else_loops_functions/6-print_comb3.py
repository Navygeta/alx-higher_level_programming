#!/usr/bin/python3
for num in range(0, 10):
    for num_2 in range(num + 1, 10):
        if not (num == 8 and num_2 == 9):
            print("{:02d}".format(num * 10 + num_2), end=", ")
        else:
            print("{:02d}".format(num * 10 + num_2), end="")


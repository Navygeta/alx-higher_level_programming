#!/usr/bin/python3
"""
Function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads contents of a file and prints to stdout

    Args:
        filename (str): File to open and print from
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

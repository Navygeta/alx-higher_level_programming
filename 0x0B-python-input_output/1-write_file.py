#!/usr/bin/python3
"""
Function that writes text to a file (UTF8) and returns chars written to stdout.
"""


def write_file(filename="", text=""):
    """
    Writes contents to a file and returns chars to stdout

    Args:
        filename (str): File to write to
        text (str): Contents to write to file

    Return:
        Chars written to file
    """
    with open(filename, "w" encoding="utf-8") as file:
        return file.write(text)

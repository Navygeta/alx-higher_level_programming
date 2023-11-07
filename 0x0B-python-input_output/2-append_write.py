#!/usr/bin/python3
"""
Function that appends text to end of the file
"""


def append_write(filename="", text=""):
    """
    Appends contents to the end of file and returns chars to stdout

    Args:
        filename (str): File to append and  write to
        text (str): Contents to append and write to file

    Return:
        Chars written and appended to file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

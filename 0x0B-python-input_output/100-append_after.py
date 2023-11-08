#!/usr/bin/python3
"""
Function that inserts a line of text to a file, after each
line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts text after each line containing a
    given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in the file.
        new_string (str): The string to be inserted.
    """
    text = ""
    with open(filename, "r") as _read:
        for line in _read:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as _write:
        _write.write(text)

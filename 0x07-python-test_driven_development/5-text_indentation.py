#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): Input text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']

    line = ""
    for char in text:
        line += char
        if char in delimiters:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())

#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""
import sys

save_to_json_file = import save_to_json_file
load_from_json_file = import load_from_json_file

try:
    py_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    py_list = []

py_list.extend(sys.argv[1:])
save_to_json_file(py_list, "add_item.json")

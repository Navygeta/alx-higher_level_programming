#!/usr/bin/python3

import sys
"""
Function that executes a function safely.
"""


def safe_function(fct, *args):

    try:
        result = fct(*args)
    except Exception as excep_err:
        print("Exception: {}".format(excep_err), file=sys.stderr)
        return None
    else:
        return result

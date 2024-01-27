#!/usr/bin/python3
"""
SCript that Fetches https://intranet.hbtn.io/status.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()

        print("Body response:$")
        print("\t- type: {}".format(type(content)) + "$")
        print("\t- content: {}".format(repr(content)) + "$")
        print("\t- utf8 content: {}".format(content.decode('utf-8')) + "$")

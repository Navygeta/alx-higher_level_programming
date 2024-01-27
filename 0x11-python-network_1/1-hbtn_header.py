#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    target_url = sys.argv[1]

    req = urllib.request.Request(target_url)
    with urllib.request.urlopen(req) as resp:
        print(dict(resp.headers).get("X-Request-Id"))

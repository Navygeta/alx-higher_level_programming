#!/usr/bin/python3
"""
SCript that Fetches https://intranet.hbtn.io/status.
"""

import urllib.request


def fetch_url_content(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        return body


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    content = fetch_url_content(url)

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("utf-8")))

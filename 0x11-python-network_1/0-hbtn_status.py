#!/usr/bin/python3
"""
SCript that Fetches https://intranet.hbtn.io/status.
"""

import urllib.request

if __name__ == "__main__":
    target_url = "https://intranet.hbtn.io/status"

    url_request = urllib.request.Request(target_url)

    with urllib.request.urlopen(url_request) as url_response:
        response_body = url_response.read()

        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode("utf-8")))

#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sy.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))

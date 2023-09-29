#!/usr/bin/python3
"""script that takes in a URL, sends a request to URL"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    reques = urllib.request.Request(argv[1])
    with urllib.request.urlopen(reques) as response:
        print(response.getheader("X-Request-Id"))

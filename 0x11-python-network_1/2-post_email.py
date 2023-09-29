#!/usr/bin/python3
"""script that takes in a URL and email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')

    reques = urllib.request.Request(url, data)
    with urllib.request.urlopen(reques) as response:
        print(response.read().decode('utf-8'))

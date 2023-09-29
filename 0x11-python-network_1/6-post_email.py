#!/usr/bin/python3
"""sends a POST request to passed URL with the email"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    val = {"email": argv[2]}
    reques = requests.post(url, data=val)
    print(reques.text)

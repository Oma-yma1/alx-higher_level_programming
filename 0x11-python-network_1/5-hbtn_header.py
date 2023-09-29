#!/usr/bin/python3
"""displays the value of  variable X-Request-Id"""
import requests
from sys import argv


if __name__ == "__main__":
    reques = requests.get(argv[1])
    print(reques.headers.get("X-Request-Id"))

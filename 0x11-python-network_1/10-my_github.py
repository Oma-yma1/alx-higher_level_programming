#!/usr/bin/python3
"""takes your GitHub credentials (username and password"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    reques = requests.get("https://api.github.com/user", auth=auth)
    print(reques.json().get("id"))

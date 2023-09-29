#!/usr/bin/python3
"""script that takes in a URL, sends a request t URL"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)

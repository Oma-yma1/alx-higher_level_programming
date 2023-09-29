#!/usr/bin/python3
"""script fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        urlb = resp.read()
        print('Body response:')
        print("\t- type: {}".format(type(urlb)))
        print("\t- content: {}".format(urlb))
        print("\t- utf8 content: {}".format(urlb.decode('utf-8')))

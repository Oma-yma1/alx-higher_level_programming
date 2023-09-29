#!/usr/bin/python3
"""request model"""

if __name__ == '__main__':
    import requests
    reques = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(type(reques.text)))
    print("\t- content: {}".format(reques.text))

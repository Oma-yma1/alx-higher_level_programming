#!/usr/bin/python3
def uppercase(str):
    str_char = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            up_char = chr(ord(char) - 32)
        else:
            up_char = char
        str_char += up_char
    print("{}".format(str_char))

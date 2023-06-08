#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argv = sys.argv[1:]
    argc = len(argv)
    for i in range (argc):
        sum = sum + int(argv[i])
    print(sum)

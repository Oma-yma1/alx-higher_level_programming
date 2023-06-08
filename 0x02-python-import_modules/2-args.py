#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(argc))
        for i in range(0, argc):
            print("{}: {}".format(i + 1, argv[i]))



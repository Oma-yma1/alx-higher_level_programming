#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbr = 0
    try:
        for j in range(x):
            print("{}".format(my_list[j]), end="")
            nbr = nbr + 1
    except IndexError:
        pass
    print("")
    return (nbr)

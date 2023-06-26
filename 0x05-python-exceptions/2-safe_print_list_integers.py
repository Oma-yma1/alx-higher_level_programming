#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nbr = 0
    for j in range(x):
        try:
            if isinstance(my_list[j], int):
                print("{:d}".format(my_list[j]), end="")
                nbr = nbr + 1
        except IndexError:
            print()
            return (nbr)
    print()
    return (nbr)

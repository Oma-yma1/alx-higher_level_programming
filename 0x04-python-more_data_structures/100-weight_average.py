#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return(0)
    else:
        total_scr = 0
        total_wei = 0
        for tup in my_list:
                total_scr = total_scr + (tup[0] * tup[1])
                total_wei = total_wei + tup[1]
        weight_av = total_scr / total_wei
        return(weight_av)

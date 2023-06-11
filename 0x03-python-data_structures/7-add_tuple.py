#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = tuple_a + (0, 0)
    b0 = tuple_b + (0, 0)
    return(a0[0] + b0[0], a0[1] + b0[1])

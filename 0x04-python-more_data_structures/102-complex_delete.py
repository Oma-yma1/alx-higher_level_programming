#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            delete.append(i)
    for i in delete:
        del a_dictionary[i]
    return(a_dictionary)        

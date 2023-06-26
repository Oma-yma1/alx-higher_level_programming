#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lis_nw = []
    for j in range(list_length):
        try:
            result = float(my_list_1[j]) / float(my_list_2[j])
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ValueError:
            print("could not convert string to float:", my_list_2[j])
            result = 0
        finally:
            lis_nw.append(result)
    return (lis_nw)

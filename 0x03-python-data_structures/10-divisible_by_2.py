#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    z = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            z[count] = True
        else:
            z[count] = False
    return(z)

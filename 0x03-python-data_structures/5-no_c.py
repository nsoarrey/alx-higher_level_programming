#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        L = list(my_string)
        L1 = ["c", "C"]
        for i in range(len(L) - 1):
            if L[i - 1] in L1:
                del L[i - 1]
        my_string = "".join(L)
    return my_string

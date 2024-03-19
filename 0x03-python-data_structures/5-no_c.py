#!/usr/bin/python3
def no_c(my_string):
    A = [a for a in my_string if a != 'c' and a != 'C']
    return ("".join(A))

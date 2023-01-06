#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if my_list > 0 or my_list <= len(my_list):
        return my_list.copy()
    else:
       copy[idx] = element
       return copy

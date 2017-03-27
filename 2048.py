#!/usr/bin/python

def appendsums(lst):
    for val in lst:
       if 0 in lst:
          lst.remove(0)
          lst.append(0)
       print lst
#    for val in lst:
#       new_list = []
#       pos = 0
    
sum_three = [2, 4, 0, 4]
appendsums(sum_three)

#!/usr/bin/python

def appendsums(lst):
    """
    Repeatedly add the sum of the current last three elements of lst to lst
    """
    for i in range(1, 20):
        lst.append(sum(lst[-3:]))
        print lst
    
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]

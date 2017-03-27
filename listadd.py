#!/usr/bin/python



def sumtree(L):
    tot = 0
    for x in L: # For each item at this level
        if not isinstance(x, list):
            tot += x # Add numbers directly
            print ("First Fn")
            print tot
        else:
            tot += sumtree(x) # Recur for sublists
            print ("Second Fn")
            print (tot)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrary nesting
print(sumtree(L))

#!/usr/bin/python

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    """
    Function to create a list with Zero moved to the end
    """
    
    for val in line:
        if 0 in line:
            line.remove(0)
            line.append(0)
    """
    Function to merge the adjacent number.
    """
    
    for i in range(0,len(line)-1):
        if line[i] == line[i+1]:
            line[i] = line[i] + line[i+1]
            for r in range(i+1,len(line)-1):
                line[r] = line[r+1]
            line[len(line)-1] = 0
    print line
    return [line]

a = [2,4,0,4]

merge(a)

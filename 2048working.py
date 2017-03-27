#!/usr/bin/env python

def merge(l):
    for i in range(len(l)):
        idx = i
        prev = i - 1
        print prev
        if prev < 0:
            continue
        if l[idx] == l[prev]:
            l[prev] = l[prev]*2
            l[idx] = 0;
            if idx+1 < len(l):
                l[idx] = l[idx+1]
                l[idx+1] = 0
    print l

l = [2,4,4,4]
merge(l)

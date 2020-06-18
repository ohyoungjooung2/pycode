#!/usr/bin/env python3
def rtriangle(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end='')
        print()

n=6
rtriangle(n)

def odd_rtriangle(n):
    for i in range(1,n+1,2):
        for _ in range(i):
           print("*",end='')
        print()

n=6
odd_rtriangle(n)

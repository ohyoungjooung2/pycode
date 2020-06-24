#!/usr/bin/env python3
#This funciton disply like below.
#When n is 5
#
#1
#2 6
#3 7 10
#4 8 11 13
#5 9 12 14 15
def numrtriangle(n):
    for row in range(n):
        val = row+1
        dec = (n-1);
        for col in range(row+1):
            print(val,end=' ')
            val += dec;
            dec -= 1
            #print(j+1,end='')
            #print("*",end='')
        print()

n=5
numrtriangle(n)

#!/usr/bin/env python3
#n is same with each n**len(str(n))'s sum.
#153 is armstrong num,cause (1**3)+(5**3)+(3**3)=>153, so 153 is armstrong num.
#First method
def armOrNot(n):
    r=0
    sn=str(n)
    nlen=len(sn)
    for i in sn:
        r+=(int(i)**nlen)
    if r == n:
       print(f'{n} is armstrong numbber')
    else:
       print(f'{n} is not armstrong numbber')

#for i in range(10000):
#    armOrNot(i)
armOrNot(153)

#Second method
def isArmstrong(n):
    r=0
    nr=n
    nlen=len(str(n))
    while(nr != 0):
        t=nr%10
        r=r+(t**nlen)
        nr=nr//10
    if (r == n):
        print(f'{n} is armstrong number')
    else:
        print(f'{n} is not armstrong number')

isArmstrong(153)

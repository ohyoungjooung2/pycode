#!/usr/bin/env python3
#n is same with each n**len(str(n))'s sum.
#153 is armstrong num,cause (1**3)+(5**3)+(3**3)=>153, so 153 is armstrong num.
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

for i in range(10000):
    armOrNot(i)

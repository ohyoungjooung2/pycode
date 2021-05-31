#https://www.hackerrank.com/challenges/cut-the-sticks/problem
def st(n):
    from collections import Counter
    b=dict(Counter(sorted(n)))
    r=[]
    r.append(len(n))
    tlen=len(n)
    for k,v in b.items():
        if tlen-v != 0:
           r.append(tlen-v)
           tlen=tlen-v
    return r


#a=[1,2,2,3,3,4]
a=[1]
a=[1,2,2,3,3,4]
a=[5,4,4,2,2,8]

print(st(a))
        
    


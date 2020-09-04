#Find pair count. below ar pair count would be
#(10,10),(10,10),(20,20)=>count is 3
ar=[10,20,20,10,10,30,50,10,20]
ar=[6,5,2,3,5,2,2,1,1,5,1,3,3,3,5]

def findpaircn(ar):
    from collections import Counter
    d=dict(Counter(ar))
    print(d)
    r=0
    for v in d.values():
        if v >= 2:
            r+=(v//2)
    return r
           


print(findpaircn(ar))

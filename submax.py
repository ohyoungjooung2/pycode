#Get submaray -1 , 0 difference of arrays
def submaxarr(a):
    from collections import Counter
    s = dict(Counter(a))
    maxv = 0
    bigger=0
    smaller=0
    for k,v in s.items():
        if v > maxv:
           maxv = v
           maxk = k
    for i in a:
        if maxk - i == 1:
           bigger+=1
        if maxk - i == -1:
           smaller+=1
    if bigger >= smaller:
        maxv += bigger
    else:
        maxv += smaller

    return maxv

def submax2(a):
    a = sorted(a)
    maxv = 0
    for i in a:
        c = a.count(i)
        d = a.count(i-1)
        c = c+d
        if c > maxv:
            maxv = c
    return maxv
           

a=[1,3,3,4,5,6,2]
print(submaxarr(a))
print(submax2(a))
a=[1,1,2,2,4,4,5,5,5,6,6,6,6]
print(submaxarr(a))
print(submax2(a))
a=[1,2,2,3,1,2]
print(submax2(a))
print(submaxarr(a))

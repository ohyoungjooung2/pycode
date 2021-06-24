#https://www.hackerrank.com/challenges/strong-password/problem
def minpass(n,pa):
    osize=len(pa)
    #pa=set(pa)
    #ssize=len(pa)
    d=0
    lc=0
    uc=0
    schr=0
    l=6
    sc = "!@#$%^&*()-+"
    for i in pa:
        if i.isdigit() == True:
            d+=1
        #print(d)
        if i.islower() == True:
            lc+=1
        #print(d)
        if i.isupper() == True:
            uc+=1
        if i in sc:
            schr+=1
    if d >= 1:
       d=1
    if lc >= 1:
       lc=1
    if uc >= 1:
       uc=1
    if schr >= 1:
       schr=1
    final_count = d+lc+uc+schr
    #return final_count
    #return d
    tobe_add_n = 4-final_count
    if osize+tobe_add_n > l:
       return tobe_add_n
    elif osize+tobe_add_n <= 6:
       return l-osize
    

print(minpass(5,'2bb'))
print(minpass(5,'2bb#A'))
print(minpass(5,'Ab1'))
print(minpass(5,'#HackerRank'))
print(minpass(5,'7900'))

#https://www.hackerrank.com/challenges/find-digits/problem
def fd(n):
    strn=str(n)
    f=0
    for s in strn:
        if int(s) >= 1 and n % int(s) == 0:
            f+=1
    return f

n=124
n=10
print(fd(n))


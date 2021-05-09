#https://www.hackerrank.com/challenges/permutation-equation/problem
def pm(p):
    minp=min(p)
    maxp=max(p)+1
    ran = []
    for i in range(minp,maxp):
        ran.append(i)
    #return ran
    ran2 = []
    for j in ran:
        ran2.append(p.index(j)+1)
    #return ran2
    ran3 = []
    for k in ran2:
        ran3.append(p.index(k)+1)
    return ran3

p=[5,2,1,3,4]
print(pm(p))

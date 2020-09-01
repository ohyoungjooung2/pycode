#https://www.hackerrank.com/challenges/the-birthday-bar/problem
#From s[0] to s[n-1]
#If sum m(3) times from s[i] consecutively and the sum is same with d
#Then increse count. 
#For example,below,m=3 so for 3 times from s[0] to s[2](0,1,2) and sum is 4, no count
#3 times from s[1] to s[3](1,2,3) and sum is 6, count=1
#3 times from s[2] to s[4](2,3,4) and sum is 6, count=2
#Finally return 2
s=[1,2,1,3,2]
d=6
m=3
def choco(s,d,m):
    tres=0
    for i in range(len(s)):
        tmp=s[i:m]
        #print(tmp)
        if sum(tmp) == d:
            tres+=1
        m+=1
        if m > len(s):
            break
    return (tres)

print(choco(s,d,m))

#Questions(problem?)


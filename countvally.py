#Count vally.
#Down is -1 , level is 0, so count -1,0 patterns.
#D=-1,U=1
#https://www.hackerrank.com/challenges/counting-valleys/problem
#Python3 example
s='UDDDUDUU'
def cntvally(s):
    s=list(s)
    for i in range(len(s)):
        if s[i] == 'U':
           s[i] = 1
        if s[i] == 'D':
           s[i] = -1
    print(s)
    res=[]
    sum=0
    for j in range(len(s)):
        sum += s[j]
        if sum == 0 or sum == -1:
           res.append(sum)
    print(res)
        
    cn=0
    for i in range(len(res)):
        if i == (len(res)-1):
            break;
        if res[i]== -1 and res[i+1] == 0:
            cn+=1
    print(cn)


s='DUDU'
cntvally(s)

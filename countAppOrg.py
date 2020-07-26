#This script is for apples array, oragnes array.
#Each member of apples and oranges +a and +b.
#And count that plused result is between s and t.
#For example, below arr is calculated like
#5+(-2),5+2,5+1=>[3,7,6], among this arr, only 7 is between s(7),t(11).
#So, first num count apples is 1
#15+(5),15+(-6)=>[20,9], among this arr, only 9 is between s(7),t(11).
#So, second num count oranges is 1
#https://www.hackerrank.com/challenges/apple-and-orange/problem

#arr=[7,11,5,15,[-2,2,1],[5,-6]]
#arr=[s,t,a,b,apples,oranges]

def countAppOrg(s,t,a,b,apples,oranges):
    apps=sorted(apples)
    orgs=sorted(oranges)
    #apps=apples
    #orgs=oranges

    appRes=0
    orgRes=0
    for ai in apps:
        if (ai+a >= s) and (ai+a <=t):
           appRes+=1

    for oi in orgs:
        if (b+oi) >= s and (b+oi) <= t:
            orgRes+=1

    print(appRes)
    print(orgRes)
           


s=7
t=11
a=5
b=15
#apples=[-2,2,1]
apples=list(range(-1000000,1000000))
oranges=list(range(1000000))
#oranges=[5,-6]
countAppOrg(s,t,a,b,apples,oranges)
#1
#1

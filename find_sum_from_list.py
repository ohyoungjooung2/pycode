#This python script find index of list that sum to 't' value.

a=[1,2,3,4,5,6]
t=9
def findsum(a,t):
    for i in range(len(a)):
        for j in range(1,len(a)):
            if a[i]+a[j] == t:
                print(i,j)

findsum(a,t)

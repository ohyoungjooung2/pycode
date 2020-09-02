#This problem(question) is simple
#If sum pair is by k(below is 5) and is divisible += 1 count.
#For example, below,,(1,4),(2,3),(4,6)=>5,5,10 is divisible by k(5). So the result is 3.
ar=[1,2,3,4,5,6]
k=5
#dsp divisible sum pairs
def dsp(ar,k):
    res=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
          #print(i,j)
          if (ar[i]+ar[j])%k == 0:
              res+=1
    return res

    

print(dsp(ar,k))

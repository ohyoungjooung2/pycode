def solution(A,K):
    if A == []:
       return A

    for i in range(K):
        A.insert(0,A[-1])
        A.pop()
    return A
a=list(range(1,11))
solution(a,3)
print(solution(a,10))


r=[9,3,9,3,9,8,9]
a=[]
r.sort()
lenr=len(r)
for i in range(0,lenr-1):
    if r[i] == r[i+1]:
       r.remove(r[i])
   
    print(r)

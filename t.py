def solution(N):
    # write your code in Python 2.7
    if N == 0:
        return 1
    else:
       A = 1
       for i in range(1,N+1):
           A *= i
       print A
       A = str(A)
       L = len(A)
       Z = 0
       for a in range(L):
        Z += int(A[a])
       return Z
         

       
        

print solution(14)

                 

        

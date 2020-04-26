
def solution(X, A):
    r = 0
    X = 5
    for i in range(len(A)):
        if A[i] == X:
            print(i)
            print(X)
            r = i
        return r

A=[1,3,1,4,2,3,5,4]
X=5
print(solution(X,A))

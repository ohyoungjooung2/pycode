#Triangle and rectangle(tilted to right)
def tri(n):
    for i in range(n):
        for _ in range(0,1):
            s=" "*(n-i-1)
            print(s,"*",end=' ')
        for _ in range(0,i):
            print("*",end=' ')

        print()
tri(5)
#     * * * * * * 
#    * * * * * * 
#   * * * * * * 
#  * * * * * * 
# * * * * * * 
def tilted_rectangle(n):
    for i in range(n):
        for j in range(0,1):
            s=" "*(n-i-1)
            print(s,"*",end=' ')
        for j in range(1,n+1):
            print("*",end=' ')

        print()

tilted_rectangle(5)

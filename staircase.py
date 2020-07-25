#This script print like below of (4) value
#   *
#  **
# ***
#****
def scase(n):
    for i in range(1,n+1):
        sp=' '*(n-i)
        for j in range(i):
          if j == 0:          
             print(sp+'*',end='')
          else:
             print('*',end='')

        print()
scase(5)

import sys
import time
def sol():
    a=int(sys.argv[1])
    l=[]
    for i in range(1,a+1):
        if ((a % i) == 0):
           l.append(i)
    if sum(l)/2 == a:
       print(f'{a} is perfect number')
    else:
       print(f'{a} is not perfect number')

def sol2(a):
    l=[]
    for i in range(1,a+1):
        if ((a % i) == 0):
           l.append(i)
    if (sum(l))/2 == a:
       print(f'{a} is perfect number')
    else:
       print(f'{a} is not perfect number')

def sol3(a):
    result = 0
    for i in range(1,a):
        if (a % i)==0:
           result = result+i
    if result==a:
       print(f'{a} is perfect number')
    else:
       print(f'{a} is not perfect number')


#sol2(28)
#sol3(28)

t1 = time.perf_counter()
for i in range(1,100001):
    sol3(i)
t2 = time.perf_counter()
print(f'Finhsed in {t2-t1} seconds')

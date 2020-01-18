import time
#From 100 million  data, find target 
data = list(range(1,100000000))
target = 555

#Linear search
def l_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

t1=time.time()
print(l_search(data,target))
t2=time.time()
print("linear search took ",(t2-t1)," seconds")

#Binary search
def b_search(data,target):
    low = 0
    high = len(data)

    while low <= high:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

t1=time.time()
print(b_search(data,target))
t2=time.time()
print("binary search took ",(t2-t1)," seconds")

def b_search_recur(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return b_search_recur(data,target,low,mid-1) 
        else:
            return b_search_recur(data,target,mid+1,high)



t1=time.time()
print(b_search_recur(data,target,0,len(data)-1))
t2=time.time()
print("recursive binary search took ",(t2-t1)," seconds")


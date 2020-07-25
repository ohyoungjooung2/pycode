#This script is for finding max values in arrays.
#First array[0] would be the number of lest array[1 to n]  members.
#For example.
#If arry is [4,3,2,1,3]
#Then 4 is the count of rest array [3,2,1,3]
#The max value is 3. And the 3 is two in the rest arry so, the return value is 2


def restMaxs(arr):
    #From 0 to return res
    res=0
    #First value of array pop and save to arr
    arr.pop(0)
    arrMax = max(arr)
    for i in arr:
        if i == arrMax:
            res+=1
    return res


arry=[4,3,2,1,3]
print(restMaxs(arry))

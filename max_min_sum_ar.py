#This script return min max sum value of list(integers all)
#Example
#First sort the array(sorted method)
#a=[1,3,5,7,9], min_sum the sum value of that is excluded max value of a '9'.
#Then, sum 1+3+5+7 => 16 

#max_sum is execlusion of first 1(is min value,1)
#So the max_sum would be 3+5+7+9=>24
arr=[1,3,5,7,9]
def sum_min_max(arr):
    #First sort array
    sorted_arr=sorted(arr)
    min_sorted_arr=list(sorted_arr)
    sorted_arr.pop(0)
    max_sum = sum(sorted_arr)
    min_sorted_arr.pop(-1)
    min_sum = sum(min_sorted_arr)
    return (min_sum,max_sum)

#Return(16,24)
print(sum_min_max(arr))
new_arr=[1,3,5,7,100]
print(sum_min_max(new_arr))

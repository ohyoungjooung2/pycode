#This python script get random values from a to b, c times,  get sum values of randomly generated values and then return avg of sum values by "c value".

def get_random_avg(a,b,c):
     import random
     rs = []
     for i in range(1,c+1):
         rs.append(random.randint(a,b))
     sum_value  = sum(rs)
     return (sum_value/c)

print(get_random_avg(1,100,100))

#This script return max value from list(nested included)
#Below function returns max value 9(example)
res=[]
def max_nest(a):
    for i in a:
        if type(i) is list:
            max_nest(i)
        else:
           res.append(i)
    #print(res)
    return max(res)

a=[1,2,[3,4,8,[3,4,5,9]],5]
print(max_nest(a))

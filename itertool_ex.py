import itertools
counter = itertools.cycle([1,2,3])


print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#data = [100,200,300,400]
#daily_data = list(itertools.zip_longest(range(10),data))
#print(daily_data)


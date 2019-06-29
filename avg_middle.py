#!/usr/bin/env python3
from statistics import mean

#When you want to get avg value from list except first and last value.
#More specific example for python3 cookbook.3rd edition

def drop_first_last_avg(grades):
     first,*middle,last = grades
     return mean(middle)


data=[10,80,80,80,80,100]
print(drop_first_last_avg(data))

#https://docs.python.org/3/library/statistics.html#statistics.StatisticsError

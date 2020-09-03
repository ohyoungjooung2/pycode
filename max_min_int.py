#https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen
#First get most frequent numbers among arr: 4=>3times, 3=>3times
#Between these two numbers, return min number. So answer is 3
arr=[1,2,3,4,5,4,3,2,1,3,4]
def mn(arr):
    tmp=[]
    from collections import Counter as ct
    re=dict(ct(arr))
    max_val=max(re.values())
    for k,v in re.items():
        if v == max_val:
            tmp.append(k)
    return (min(tmp))

print(mn(arr))
    

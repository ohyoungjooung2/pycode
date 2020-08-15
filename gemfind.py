#Find common asciis among strings. And count it.
#For example, if arr=['abcdde','baccd','eeabg']
#Then, ab is all arr[0],arr[1],arr[2], so the count is 2('a',and 'b')

def gemfind(arr):
    lenar=len(arr)
    from collections import Counter
    cn=Counter()
    for s in range(lenar):
        cn+=Counter(set(arr[s]))
    cnd=dict(cn)
    rescnt=0
    for c in cnd.values():
        if c == lenar:
           rescnt+=1
    return(rescnt)

arr=['abcdde', 'baccd', 'eeabgc']
print(gemfind(arr))


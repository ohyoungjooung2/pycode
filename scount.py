#https://www.hackerrank.com/challenges/sparse-arrays/problem
#String count from queries
#aba happens 2 time, in strings
#xzxb happens 1 time in strings,
#ab happens 0 time in strings
#So this return [2,1,0]
strings=['aba','baba','aba','xzxb']
queries=['aba','xzxb','ab']
def ms(strings,queries):
    res=[]
    from collections import Counter
    sc=dict(Counter(strings))
    for q in queries:
        if q in sc:
           res.append(sc[q])
        else:
           res.append(0)
    return res


print(ms(strings,queries))


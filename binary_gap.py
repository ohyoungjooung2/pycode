def solution(n):
    # write your code in Python 3.6
    bn="{0:b}".format(n)
    #print(bn)
    rbn=bn.split('1')
    rbn.pop()
    #print(rbn)
    
 
    return len(max(rbn))

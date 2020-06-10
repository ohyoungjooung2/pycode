#Int to binary(my own)^^
def to_b(n):
     r = ''
     while n >= 1:
         ra = n % 2
         r += str(ra)
         n = n/2
     return r[::-1]
 

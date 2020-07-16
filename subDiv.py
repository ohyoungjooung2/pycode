# This script is for..
# Example
# 100->2*2*5*5,36-> 2*2*3*3
def lcm(a,b):
    #Inner def function
    def innerr(r):
      aar = []
      while r != 1:
          if r % 2 == 0:
              aar.append(2)
              r = r//2
          elif r % 3 == 0:
              aar.append(3)
              r = r//3
          elif r % 5 == 0:
              aar.append(5)
              r = r//5
          else:
              aar.append(r)
              r = 1
      return aar
    ars = innerr(a)
    brs = innerr(b)
    return (ars,brs)
print(lcm(100,36))

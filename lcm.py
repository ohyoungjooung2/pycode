# This script is for lcm(least common multiple)
def lcm(a,b):
    if a == b:
        return a
    
    #Swap if b > a
    if b > a:
        tmp = b
        b = a
        a = tmp

    # 12 % 3 == 0, then lcm is 12.
    #12,24..and 3 6 9 12..return 12.
    #print(a)
    #print(b)
    if a%b == 0:
        return a

   
    #Init higher from a
    higher=a
    while True:
        higher += a
        if higher % b == 0:
           lcm_result = higher
           break;
        else:
           lcm_result = None

    return lcm_result

print("lcm of 10002 11 is ", lcm(10002,11))
#
#a = 100,200,300,400,500,600,700,800,900...
#b = 36 72 108 144 180 216 252 288 324 360 396 432 468 504 540 576 612 648 684 720 756 792 828 864 900 936 972 1008 1044 1080 1116 1152 1188 1224 1260 1296 1332 1368 1404 >>> 
#Above least common multiple is 900..
#print(lcm(100,36))
#print(lcm(24,36))
#print(lcm(24,1000000000))
#Above will print 900
#print(lcm(12,3))
#Above will print 12
#print(lcm(3,12))
#Above will print 12

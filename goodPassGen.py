import random
import string
import time
def genGoodpass(n):
    #Generate n numbers of passwords that include at least one each lower and uppercase ascii,digit(at least one),speciat chars('!@#$%^&*()+')-at least one two
    goodPass=[]
    rc=random.choice
    sal=string.ascii_lowercase
    sau=string.ascii_uppercase
    spchar='!@#$%^&*()+'
    sd=string.digits
    passins=[sal,sau,spchar,sd]
    for i in range(n-4):
        passins.append(random.choice(passins))
    for i in passins:
        goodPass.append(rc(i))

    
    random.shuffle(goodPass)
    goodPass=''.join(goodPass)
    return goodPass
print(genGoodpass(17))

import random
import string
def genGoodpass():
    #Generate 8 passwords that include at least one each lower and uppercase ascii,digit(at least one),speciat chars('!@#$%^&*()+')-at least one two
    goodPassList=[]
    sal=string.ascii_lowercase
    sau=string.ascii_uppercase
    spchar='!@#$%^&*()+'
    sd=string.digits
    passSpc=random.choice(spchar)
    passLower=random.choice(sal)
    passUpper=random.choice(string.ascii_uppercase)
    passSpc2=random.choice(spchar)
    passLower2=random.choice(sd)
    passUpper2=random.choice(sau)
    passLower3=random.choice(sal)
    passUpper3=random.choice(sau)
    for es in (passSpc,passSpc2,passLower,passLower2,passUpper2,passUpper,passUpper3,passLower3):
        goodPassList.append(es)
    random.shuffle(goodPassList)
    goodPass=''.join(goodPassList)
    return goodPass
print(genGoodpass())



    


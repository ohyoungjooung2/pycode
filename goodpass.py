import random
import string
def genGoodpass():
    goodPassList=[]
    passSpc=random.choice('!@#$%^&*()+')
    passLower=random.choice(string.ascii_lowercase)
    passUpper=random.choice(string.ascii_uppercase)
    passSpc2=random.choice('*&()!@#$%^&')
    passLower2=random.choice(string.digits)
    passUpper2=random.choice(string.ascii_uppercase)
    passLower3=random.choice(string.ascii_lowercase)
    passUpper3=random.choice(string.ascii_uppercase)
    for es in (passSpc,passSpc2,passLower,passLower2,passUpper2,passUpper,passUpper3,passLower3):
        goodPassList.append(es)
    random.shuffle(goodPassList)
    goodPass=''.join(goodPassList)
    return goodPass
print(genGoodpass())



    


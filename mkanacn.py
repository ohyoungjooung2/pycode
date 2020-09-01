s1='cde'
s2='abc'
def mkanac(s1,s2):
    from collections import Counter
    r1=dict(Counter(s1)-Counter(s2))
    r2=dict(Counter(s2)-Counter(s1))
    res=0
    for k,v in r1.items():
        res+=v
    for k,v in r2.items():
        res+=v
    return res

s1='absdjkvuahdakejfnfauhdsaavasdlkj'
s2='djfladfhiawasdkjvalskufhafablsdkashlahdfa'
print(mkanac(s1,s2))


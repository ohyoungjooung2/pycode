#All time format(AM,PM) into 24 hour unit.
#
#s='07:05:45PM' woule be19:05:45
#s2='12:44:45AM' would be 00:44:45 
#s3='12:44:45PM' would be 12:44:45
#s4='01:44:45PM' would be 13:44:45

def timeConversion(s):
    if 'PM' in s:
        res=s.replace('PM','')
        res=res.split(':')
        ires=int(res[0])+12
        if ires == 24:
           ires = str('12')
        res[0]=str(ires)
        return ':'.join(res)
    if 'AM' in s:
        res=s.replace('AM','')
        res=res.split(':')
        if int(res[0]) == 12:
           res[0]='00'
        return ':'.join(res)

s='07:05:45PM'
s2='12:44:45AM'
s3='12:44:45PM'
s4='01:44:45PM'
print(timeConversion(s))
print(timeConversion(s2))
print(timeConversion(s3))
print(timeConversion(s4))

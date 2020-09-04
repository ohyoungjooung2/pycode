#This is leap year calculator question.
#256 day is 09.12 if the year is leap one, 09.13 if the year is not leap one.
#Exception 1918 should plus 14 days cause of between change gap.
#Kinda easy. From 1917 to present , Gregorian calendar, so the leap year is divisialbe by 400....like below..
#Exempted

year=2017
def leapyear(year):
    if (year == 1918):
        return "26.09."+str(year)
    if (year > 1917) and  ((year % 400) == 0) or (((year % 4) == 0) and ((year % 100) != 0)):
        return "12.09."+str(year)
    elif (year >= 1700) and ( year <= 1917) and ((year % 4 == 0)):
        return "12.09."+str(year)
    else:
        return "13.09."+str(year)

year=2016
#year=1800
#year=2017
print(leapyear(year))

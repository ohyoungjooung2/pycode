#!/usr/bin/env python3
#This script calculates your age till seconds..your age starts 00:00 
import datetime
#Just modify below line for your birthday..
BIRTHDAY='1972,01,12'

HOUR_IN_SEC=(60*60)
DAY_IN_SEC=(HOUR_IN_SEC*24)
YEAR_IN_SEC=(DAY_IN_SEC*365)

#date of birth in seconds
def age_in_sec(dob='1972,01,12'):
    #date of birth into sec(string)
    dobs=datetime.datetime.strptime(dob,'%Y,%m,%d').strftime('%s')
    #dob into integer for calculation
    dobi=int(dobs)

    #Now sec into integer from string
    nowi=int(datetime.datetime.today().strftime('%s'))

    AGE_IN_SEC=(nowi-dobi)
    #print("You are living for " + str(AGE_IN_SEC) + " seconds")
    return AGE_IN_SEC



#ais=mybirthday..^^
def age_till_seconds(ais='1972,01,12'):
    AGE_IN_SEC=age_in_sec(ais)
    if int(AGE_IN_SEC) < YEAR_IN_SEC:
        print("You are younger than 1 year")
    elif int(AGE_IN_SEC) >= YEAR_IN_SEC:
        AGE=(AGE_IN_SEC//(YEAR_IN_SEC))
        REMAIN_SEC=(AGE_IN_SEC % YEAR_IN_SEC)
        #If REMAIN_SEC is more than DAY_IN_SEC(24*60*60) we can get remain days,hours,minutes and seconds
        if REMAIN_SEC > DAY_IN_SEC:
           #Remain days
           AGE_RDAYS=(REMAIN_SEC//DAY_IN_SEC)
           #Remain hours
           REMAIN_HOUR=(REMAIN_SEC%DAY_IN_SEC) // HOUR_IN_SEC
           #Remain minutes
           REMAIN_MINUTES=((REMAIN_SEC%DAY_IN_SEC) % HOUR_IN_SEC) // 60
           #Remain seconds
           REMAIN_SECONDS=((REMAIN_SEC%DAY_IN_SEC) % HOUR_IN_SEC) % 60
           print("You are "+ str(AGE) + " year(s) " + str(AGE_RDAYS) + " day(s) " + str(REMAIN_HOUR) + " hour(s) " + str(REMAIN_MINUTES) + " minute(s) " + str(REMAIN_SECONDS) + " second(s) " + "old")
        else:
           print("You are "+ str(AGE) + "  " + "years old")
        
        
age_till_seconds('2019,02,04')

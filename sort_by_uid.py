#!/usr/bin/python3
#This short python3 script to sort /etc/passwd file by uid
P='/etc/passwd'
pfile=open(P,'r')
#pfile is in list
pfile=pfile.readlines()

#sortbyuid
sortbyuid=lambda sbu: int(sbu.split(':')[2])
pfile.sort(key=sortbyuid)
#print after strip '\n' character
for line in pfile:
    print(line.strip())

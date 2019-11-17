#!/usr/bin/env python3
#Simple example to download one file using python3.
#Filename to down
FN='vim81w32.zip'
LOCALFILE="/tmp/" + FN
FTPSITE='ftp.kr.freebsd.org'
FTPDIR='/pub/vim/pc/'
FTPUSER='anonymous'
FTPPASS='anonymous'

#Import ftp lib
from ftplib import FTP

ftp = FTP(FTPSITE)
ftp.login(user=FTPUSER,passwd=FTPPASS)
ftp.cwd(FTPDIR)

def downFile():
    print("Downloading " + FN + "file")
    #For unix like(Linux)
    localfile=LOCALFILE
    #For windows
    #localfile="c:\\tmp\\" + FN
    localfile = open(localfile,'wb')
    ftp.retrbinary('RETR ' + FN, localfile.write, 1024)
    ftp.quit()
    localfile.close()


#For upload
#def placeFile():
#    filename = 'test.txt'
#    ftp.storbinary('STOR '+filename, open(filename,'rb'))
#    ftp.quit()


#Execute downfile
downFile()

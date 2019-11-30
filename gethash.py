#!/usr/bin/env python3
#Get file hash md5 sha256 sha512 of directories, python2 ok.
import os
import stat
import hashlib
def getFileHash(dirname,m):
    if os.path.exists(dirname):
       dirfiles=os.listdir(dirname)
       for files in dirfiles:
           files=dirname+"/"+files
           #Socket file check method
           mode = os.stat(files).st_mode
           isSocket = stat.S_ISSOCK(mode)
           if (os.path.isdir(files) == False) and (isSocket == False):
               with open(files,'rb') as gethash:
                   data = gethash.read()
                   if m == "sha256":
                     gethash = hashlib.sha256(data).hexdigest()
                     print(files + ": " + gethash)
                   elif m == "md5":
                     gethash = hashlib.md5(data).hexdigest()
                     #To comply with windows get-filehash us upper() method
                     #print(files + ": " + gethash.upper())
                     print(files + ": " + gethash)
                   elif m == "sha512":
                     gethash = hashlib.sha512(data).hexdigest()
                     print(files + ": " + gethash)
    else:
        print('path doesnot exist')

#Get result
getFileHash('/tmp','sha512')
#getFileHash('/tmp','sha256')
#getFileHash('/tmp','md5')

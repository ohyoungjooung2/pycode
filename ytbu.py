# -*- conding: utf-8 -*-
import os
import subprocess
import pytube
import sys
 
if not os.path.exists("download"):
    os.mkdir("download")
 
#url = input("link : ")
url = sys.argv[1]
yt = pytube.YouTube(url)
print(yt.title)
 
vids= yt.streams.all()
#vids= yt.streams.desc()
 
for i in range(len(vids)):
    print(i,'. ',vids[i])
 
vnum = int(input("resolution "))
#vnum = int(1)
 
parent_dir = "./"
dstfile = "./download/" + sys.argv[1]
 
try:
    vids[vnum].download(parent_dir)
    os.rename("download/YouTube.mp4", dstfile)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
 
print('down ok!')

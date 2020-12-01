#This script split binary file into 1mb
#Here just test.mp3. Should change this file name.
#Also CH_SIZE can be changed to bigger or smaller
#This is binary file splitter
import sys
import os
CH_SIZE=int(sys.argv[1])
FILENAME=str(sys.argv[2])
OUTPUT="./"+FILENAME+"_"+"output"
CUDIR=os.getcwd()
if os.path.exists(OUTPUT)==False:
    os.mkdir(OUTPUT)

file_number=1
with open(FILENAME,'br') as f:
    chunk = f.read(CH_SIZE)
    while chunk:
        os.chdir(OUTPUT)
        with open(FILENAME+'_part_'+str(file_number),'bw') as chk_file:
            chk_file.write(chunk)
        os.chdir(CUDIR)
        file_number += 1
        chunk = f.read(CH_SIZE)

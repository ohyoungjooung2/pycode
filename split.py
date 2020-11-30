#This script split binary file into 1mb
#Here just test.mp3. Should change this file name.
#Also CH_SIZE can be changed to bigger or smaller
CH_SIZE=1048576
file_number=1
with open('test.mp3','br') as f:
    chunk = f.read(CH_SIZE)
    while chunk:
        with open('test.mp3_part_'+str(file_number),'bw') as chk_file:
            chk_file.write(chunk)
        file_number += 1
        chunk = f.read(CH_SIZE)

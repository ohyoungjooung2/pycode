#This python script change jpg image into png image
#If directory pngs not exists, then create.
import os
from PIL import Image, ImageFilter
IMAGEDIR='./images'
#File size designation
SIZE_300 = (300,300)

#If pass directory not exists, then creat IMAGDDIR
if os.path.exists(IMAGEDIR) == False: 
   os.mkdir(IMAGEDIR)
else:
   pass

#If IMAGEDIR ALREADY EXISTS BUT THAT IS FILE , THEN REMOVE AND CREATE IMAGEDIR
if os.path.isdir(IMAGEDIR) == False:
   print(IMAGEDIR,"is not directory, remove and create directory ",IMAGEDIR)
   os.remove(IMAGEDIR)
   os.mkdir(IMAGEDIR)
else:
   pass

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn,fext = os.path.splitext(f)
        if(os.path.exists(IMAGEDIR+'/{}_300{}'.format(fn,fext)) == False):
           i.thumbnail(SIZE_300)
           i.save(IMAGEDIR+'/{}_300{}'.format(fn,fext))
        else:
           pass
           #print(IMAGEDIR+'/{}_300{}'.format(fn,fext) + " alreay exists")

#Image rotation
rimage1=Image.open('./2.jpg')
rimage1.rotate(90).save('2_rotated.jpg')

#Image black and white
rimage1.convert(mode='L').save('2_mod.jpg')
#Image blur
rimage1.filter(ImageFilter.GaussianBlur(13)).save('2_blurred.jpg')

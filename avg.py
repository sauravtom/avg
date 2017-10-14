
"""
============================================================
              AVG: Artistic Video Generator
Converts photos into artistic videos & gifs

============================================================
"""
#imports 
from PIL import Image
from collections import defaultdict
import argparse
import time
import os
import time
import random
import pdb

from utils import download_image, styletransfer

print("")
print("***********************************************")
print("                 AVG v1.0                  ")
print("Converts photos into artistic videos & gifs")
print("***********************************************")

#options
parser = argparse.ArgumentParser(description='AVG v1.0')
parser.add_argument('-i','--image',help='Source image path',required=True)
parser.add_argument('-o' ,'--savepath',help='output path',required=True)
parser.add_argument('-f','--frames',help='Number of frames in output | Default is 6',type=int,default=6)
parser.add_argument('-d','--delay',help='morphing time interval | Default is 5',type=int,default=5)
parser.add_argument('-v','--video',help='get video as output as well | Default is Flase',type=bool,default=False)

args = parser.parse_args()

start = time.time()  

temp_file_prefix='styled_'
temp_dir='temp'
original_image='%s/%s0.jpg'%(temp_dir,temp_file_prefix)

try:
    img = Image.open(args.image)
except:
    print("ERROR:Unable to open image!")  
    exit()

#numeric list of styles available at http://turbo.deepart.io/styles/
style_list="1,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,47"
style_list=style_list.split(',')

#looping in a list of n number of random styles where n is the number of frames(default 6)
for i in random.sample(style_list, args.frames):
    temp_file_path = styletransfer(file_name=args.image,file_path=args.image,
            style_number=i,output_dir=temp_dir,temp_file_prefix=temp_file_prefix)

#resize input image the same as the rest
im2=Image.open(temp_file_path)
width, height = im2.size
resized_img = img.resize((width,height), Image.ANTIALIAS)
resized_img.save(original_image)

#combine all images into a gif
os.system("convert %s temp/%s* %s -delay %s -morph 10 %s"%(original_image,temp_file_prefix,original_image,args.delay,args.savepath))

if args.video:
    os.system("ffmpeg -f gif -i %s %s"%(args.savepath,'output.mp4'))

#converting mp4 back to gif
#ffmpeg -i input.mp4 -vf scale=320:-1 -r 10 -f image2pipe -vcodec ppm - | convert -delay 5 -loop 0 - output.gif

os.system("rm temp/*")
print ('Elaspsed ',time.time() - start, 'sec') 



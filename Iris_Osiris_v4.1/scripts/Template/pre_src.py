# -*- coding: utf-8 -*-
import cv2
import os
import numpy
#import cutHumanFace
import shutil


# import os,shutil,string
# dir = '/home/tt-ava/test'    
# for i in os.listdir(dir):
#     newfile = i.replace('.','_')  
#     oldname = dir +'/'+str(i)
#     newname = dir +'/'+str(newfile)
#     shutil.move(oldname,newname) 

if __name__ == '__main__':
    base_dir = '/mnt/pigeon3/'
    dest_dir = '/mnt/pigeon4/'
    list_txt = '/mnt/Iris_Osiris_v4.1/scripts/Template/pigeon.txt'
    # mathing_txt = '/mnt/Iris_Osiris_v4.1/scripts/Matching/matching_all.txt'
    with open(list_txt, 'w') as f:
	    for i in os.listdir(base_dir):
	        for j in os.listdir(base_dir + i):
	        	file = i+'_'+j
	        	print file
	        	shutil.copy(os.path.join(base_dir, i, j), os.path.join(dest_dir, file))
	        	f.write(file+'\n')






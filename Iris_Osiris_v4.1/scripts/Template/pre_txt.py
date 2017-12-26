# -*- coding: utf-8 -*-
import cv2
import os
import numpy
#import cutHumanFace
import shutil
import glob

if __name__ == '__main__':
    base_dir = '/mnt/data/pigeon_resized/'

    with open('/mnt/Iris_Osiris_v4.1/scripts/Template/pigeon_new.txt', 'w') as t:
    	f = glob.glob(base_dir+'*')
    	f = sorted(f, key=lambda x : int(x.split('/')[-1].split('_')[0]))
    	print f
    	for x in f:
    		t.write(x.split('/')[-1]+'\n')





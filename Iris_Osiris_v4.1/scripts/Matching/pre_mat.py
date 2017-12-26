# -*- coding: utf-8 -*-
import cv2
import os
import numpy
import shutil



if __name__ == '__main__':
    dest_dir = '/mnt/data/pigeon_resized/'
    list_txt = '/mnt/Iris_Osiris_v4.1/scripts/Matching/list_matching.txt'
    # 比较相邻两张图片
    with open(list_txt, 'w') as f:
    	lst = os.listdir(dest_dir)
    	slst = sorted(lst, key = lambda x : int(x.split('_')[0]))
    	pre = slst[0]
        for i in slst[1:]:
            if i.split('_')[0] == pre.split('_')[0]:
                print (1, pre, i)
            else:
                print (2, pre, i)
            f.write(pre+' '+i+'\n')
            pre = i






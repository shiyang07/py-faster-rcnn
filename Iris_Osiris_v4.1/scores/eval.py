# -*- coding: utf-8 -*-
import cv2
import os
import numpy
import shutil
import glob


if __name__ == '__main__':
    list_txt = '/mnt/Iris_Osiris_v4.1/scores/score_new.txt'

    ttm = 0        #同一只鸽子，同一只眼睛
    m = 0

    tn = 0      #同一只鸽子，或者不同鸽子，不同的眼睛（左右）
    n = 0

    sd = 0   #同一只鸽子，不同眼睛
    d = 0    

    thre = 0.4

    for x in open(list_txt, 'r').read().split('\n'):
    	#print x.split(' ')
    	if len(x.split(' ')) < 2:
    		continue

    	l, r, score = x.split(' ')[0], x.split(' ')[1], float(x.split(' ')[2])
    	
    	if score == 1.0:
    		continue
		l = l.split('_'); r = r.split('_')

		if l[0] = r[0]:
			sd += 1
			if l[1] != r[1] and score < thre:
				d += 1
			elif l[1] == r[1] and score < thre:


		else:






    	if 
			print l.split('_')[:2], r.split('_')[:2], score, 11111111111, '\n'
    	else:
			print l.split('_')[:2], r.split('_')[:2], score, 22222222222, '\n'

    	if l.split('_')[:2] == r.split('_')[:2] and score < 0.45:
    		ttm += 1
    		m += 1
    	elif l.split('_')[:2] == r.split('_')[:2]:
    		m += 1
    	else:
    		n += 1
    		if score >= 0.4:
    			tn += 1
    print ttm, tn, m, n
    print "相同鸽子，同一只眼睛的验证准确率", float(ttm / m)
    print "相同鸽子，左右眼睛相似性在0.4以内的概率", float(ttm / m)

    print "不同鸽子眼睛的验证准确率", float(tn / n)












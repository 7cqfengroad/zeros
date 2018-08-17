# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:01:52 2018

@author: feng
"""

import shutil
import os
import pandas as pd


def generate_train():
    path = 'for_train'
    
    if os.path.exists(path):
        shutil.rmtree(path)
    
    f = open('train.txt', "r")
    lines = f.readlines()
    for line in lines:
        l = line.strip().split('\t')
        fname = l[0]
        breed = l[1]
        path2 = '%s/%s' % (path, breed)
        if not os.path.exists(path2):
            os.makedirs(path2)
        shutil.copyfile('F:/zero/data/DatasetA_train_20180813/train/%s' % fname, '%s/%s' % (path2, fname))   #创立软连接

        
        
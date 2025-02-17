# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:08:54 2024

@author: barsd
"""

import sys, string, os
import pandas as pd
import numpy as np
import cv2
import csv
import shutil 

def load_images_from_folder(folder):
    images = []
    file_name=[]
    for filename in os.listdir(folder):
        file=os.path.join(folder,filename)
        img = cv2.imread(file)
        if img is not None:
            images.append(img)
            file_name.append(filename)
    return images,file_name

def train_haarcascade(Path1):

    Path2=Path1+"/opencv/build/x64/vc15/bin/"
    

    my_file1 = os.path.isfile(Path1+"/pos.txt")
    if not (my_file1):
        cmd1=Path2+"opencv_annotation.exe --annotations=pos.txt --images=positives/"
        os.system(cmd1)

    my_file2 = os.path.isfile(Path1+"/neg.txt")
    my_file3 = os.path.isfile(Path1+"/pos.vec")
    if not (my_file1 and my_file2 and my_file3):
        cmd2=Path2+"/opencv_createsamples.exe -info pos.txt -bg neg.txt -vec pos.vec -w 36 -h 24 "
        os.system(cmd2)
    neg=0

    with open(Path1+'/neg.txt', 'w') as f:
        for filename in os.listdir(Path1+'/negatives'):
            neg+=1
            f.write(Path1+'/negatives/' + filename + '\n')

    pos=0
    with open(Path1+'/pos.txt') as f:
        lines=[line for line in f]
        for i in lines:
            splt=i.split()
            pos+=int(splt[1])
    pos=int(0.9*pos)
    my_file4 = os.path.isdir(Path1+"/cascade_dir")
    directory = Path1+"/cascade_dir"
    parent_dir=Path1
    directory = os.path.join(parent_dir, directory)

    if not(my_file4):
      os.mkdir(directory)
      cmd3=Path2+"/opencv_traincascade.exe -data "+directory+" -info pos.txt -vec pos.vec -bg neg.txt -numPos "+pos+" -numNeg "+neg+" -w 36 -h 24 -numStages 15 -minHitRate 0.9"
      os.system(cmd3)

    finalCascadeFile = directory+'/cascade.xml'

path="THE MAIN PATH OF PROJECT"
train_haarcascade(path)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 21:26:52 2022

@author: barış
"""

import cv2,os,csv
from skimage import io
import pandas as pd


def get_iou(bb1, bb2):
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])
    if x_right < x_left or y_bottom < y_top:
        return 0.0
    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    assert iou >= 0.0
    assert iou <= 1.0
    return iou



df = pd.read_csv(os.path.join("annotations.csv"))
path="PATH TO IMAGES"
bird_cascade=cv2.CascadeClassifier("cascade.xml")
bbox_test=[]
for e,image in enumerate(os.listdir(path)):
    image_name=path+'/'+image
    img=io.imread(image_name)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    birds=bird_cascade.detectMultiScale(gray,1.3,5)
    annot_list = [row for row in df.iterrows() if row[1][0]==image]
    for i in range(len(annot_list)):
        x1=int(annot_list[i][1][4])
        y1=int(annot_list[i][1][5])
        x2=int(annot_list[i][1][6])
        y2=int(annot_list[i][1][7])
        gtval={"x1":x1,"x2":x2,"y1":y1,"y2":y2}
        for(x,y,w,h) in birds:
        #img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            iou = get_iou(gtval,{"x1":x,"x2":x+w,"y1":y,"y2":y+h})
            if(iou>0):
                img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                #cv2.imshow('d',img)
                #cv2.waitKey(0)
                bbox_test.append([e,image,iou,x,y,w+x,h+y])
    #cv2.imshow('Detect Image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindow()

file = open('test_boxes.csv', 'w+', newline ='')
with file:     
    write = csv.writer(file) 
    write.writerows(bbox_test) 
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:06:03 2024

@author: barsd
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:41:00 2024

@author: barsd
"""

import cv2,os,csv
from skimage import io
import pandas as pd
import numpy as np
from skimage import color
from copy import deepcopy

path='PATH TO THE EMPTY FOLDER WHERE THE BLURED IMAGES WILL BE SAVED'
images_path='PATH TO ORIGINAL IMAGES'
detection_path='PATH TO THE FOLDER CONTAINING csv FILES'

image_list=[]
image_names=[]
for image in (os.listdir(images_path)):
    image_name=images_path+'/'+image
    img=io.imread(image_name)
    #img=cv2.imread(image_name,cv2.IMREAD_COLOR)
    if img is not None:
        image_list.append(img)


for file in (os.listdir(images_path)):
    image_names.append(file)


detection_list=[]
for e,files in enumerate(os.listdir(detection_path)):
    file=open(detection_path+"/"+files,'r')
    data = list(csv.reader(file, delimiter=","))
    detection_list.append(data)

result_list=[]
for e,image in enumerate(image_list):
    min_x=float('inf')
    max_x=float('-inf')
    min_y=float('inf')
    max_y=float('-inf')
    for files in detection_list:
        for row in files:
            if(row[1]==image_names[e]):
                if(int(row[3])<min_x):
                    min_x=int(row[3])
                if(int(row[4])<min_y):
                    min_y=int(row[4])
                if(int(row[5])>max_x):
                    max_x=int(row[5])
                if(int(row[6])>max_y):
                    max_y=int(row[6])
    mask = np.ones_like(image)
    #mask=np.bitwise_not(mask)
    color = (255, 255, 255)
    thickness = 2
    start_point=(min_x,min_y)
    end_point=(max_x,max_y)
    if(min_x>max_x and min_y>max_y):

        cv2.imwrite(image_names[e], image)
    else:

        shape0=int(image.shape[0]/20)
        shape1=int(image.shape[1]/20)
        if(shape0%2==0):
            shape0=shape0+1
        if(int(shape1%2)==0):
            shape1=shape1+1
            
        #mask=cv2.rectangle(mask, start_point, end_point, color, -1)
        #roi = image[min_y:max_y, min_x:max_x]
        mask[min_y:max_y, min_x:max_x]=255
        #cv2.imwrite(path+"/"+"Step1.jpg", mask)

        #mask[roi]=0
        
        gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray,(15,15),0)
        ret3,thresholded_img = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        mapping = cv2.cvtColor(thresholded_img, cv2.COLOR_GRAY2RGB)
        np.unique(mapping)
        blurred_original_image = cv2.GaussianBlur(image,(251,251),0)
        #cv2.imwrite(path+"/"+"Step2.jpg", blurred_original_image)

        #result = np.bitwise_or(image,mask)
        layered_image = np.where(mapping != (0,0,0), image, blurred_original_image)
        im_rgb = cv2.cvtColor(layered_image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(path+"/"+image_names[e], im_rgb)
        
        
        #image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #blur = cv2.GaussianBlur(image, (3,3),0)
        #blur=cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)
        #blur[min_y:max_y, min_x:max_x]=roi
    #result = np.bitwise_or(image,mask)
        #path2='C:\\Users\\malzeme müh\\.spyder-py3\\.spyder-py3\\Gaussian Blurring\\ADA DOĞANI'

    #cv2.imwrite(os.path.join(images_path , image_names[e]), blur)

        #cv2.imwrite(path+"/"+image_names[e], blur)
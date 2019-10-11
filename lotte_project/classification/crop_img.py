
# image에 bboxing한 부분을 croping 하는 코드.

import cv2
import numpy as np
import imutils

import xml.etree.ElementTree as ET
from PIL import Image
import os

label_path='/home/pc/Desktop/Machine_Learning/Project_Lotte/sample_data/label' # label 파일
label_list = os.listdir(label_path)
root_path='/home/pc/Desktop/Machine_Learning/Project_Lotte/sample_data/original/' # image파일
#image_folder = os.listdir(image_folder_path)

#image_sub_path = os.path.join(image_folder_path, image_folder)
#image_subdir = os.listdir(image_sub_path)
label_path = label_path + '/'

for labels in label_list:
    try:
        tree = ET.parse(label_path+labels) # parse xml files to element tree
        file_path = tree.find('path').text

        folder_name = tree.find('object/name').text
        file_name = tree.find('filename').text
        xmin = int(tree.find('object/bndbox/xmin').text)
        ymin = int(tree.find('object/bndbox/ymin').text)
        xmax = int(tree.find('object/bndbox/xmax').text)
        ymax = int(tree.find('object/bndbox/ymax').text)

        file_path = file_path.replace('\\','/')
        file_path_list = file_path.split('/')

        # Cocal Cola 오타에 대한 오류 수정.
        if file_path_list[-3] == '14_Cocal Cola Zero Can 250ml':
            file_path_list =  '14_Coca Cola Zero Can 250ml/' +file_path_list[-2] +'/'
        else:
            file_path_list = file_path_list[-3] + '/' +file_path_list[-2] +'/'

        # crop 파일이 이미 존재한다면 건너뜀.
        if (os.path.isfile(root_path + 'CropImage/' + file_path_list + file_name)):
            continue
        print(file_path_list)
        print(file_name)
        im = Image.open(root_path+file_path_list+file_name)
        crop_image = im.crop((xmin,ymin,xmax,ymax))

        if not os.path.isdir(root_path+'CropImage/'+file_path_list):
            os.makedirs(root_path+'CropImage/'+file_path_list)
        crop_image.save(root_path+'CropImage/'+file_path_list+file_name)

    except AttributeError:
        print(labels)
    except SystemError:
        print(labels)
    #except FileNotFoundError:
       # print(labels)
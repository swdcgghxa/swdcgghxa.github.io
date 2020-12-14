#!/usr/bin/env python
# coding: utf-8

#get_ipython().system('python -V')
#get_ipython().system('python -m pip install opencv-python')
#get_ipython().system('python -m pip install -U pip')
#get_ipython().system('apt install libgl1-mesa-glx')
#get_ipython().system('pip3 install opencv-python')

# In[ ]:

import os
import numpy as np
import re
import cv2
from .simple_tool import img_use_increase
# In[ ]:

DB_PATH = './40840159'
TAG_DATA = [i for i in os.listdir(DB_PATH) if i in "0987654321"]

# In[ ]:


data = {}
for _path in TAG_DATA:
    _this_dir_path = f"{DB_PATH}/{_path}"
    _this_time = []
    for item in os.listdir(_this_dir_path):
        if re.match("([0-9()]|\w)+\.jpg",item):
            _img_path = f"{_this_dir_path}/{item}"
            img = (255-cv2.imread(_img_path))/255
            img = (
                (
                    img[:,:,0] + img[:,:,1] + img[:,:,2]
                )/3
            )
            _this_time.append(
                img_use_increase(img,multiple=5,noise_removal=60)
                # 1-cv2.imread(_img_path,cv2.IMREAD_GRAYSCALE)
            )
        else:
            print("不會載入：",item)
    data[int(_path)]= _this_time

#for i in TAG_DATA:
#    print("壓縮圖已生成：",i)
#    cv2.imwrite(f"{DB_PATH}/img_{i}.jpg", np.concatenate(
#            [i * 255 for i in [ *data.get( int(i) ) ]]
#        )
#    )

import random

from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train = np.concatenate( [x_train,*data.values()] ,axis=0)
print("x_train: ",x_train.shape)
y_train = np.concatenate( [y_train,np.concatenate([np.full((len(data.get(i))),i) for i in map(lambda x:int(x),TAG_DATA)])] )
print("y_train: ",y_train.shape)
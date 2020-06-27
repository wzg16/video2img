#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/27 10:40 
# @Software: PyCharm
# @Author : wzg16
"""
@File : imgs2video.py
@Function:

"""
import cv2
import os
import glob

imgs_dir = './frames'
video_path = './video.avi'

img_list = glob.glob(os.path.join(imgs_dir,"*.jpg"))
print(len(img_list))

fps = 100
H,W = 256,500

fourcc = cv2.VideoWriter_fourcc(*"MJPG")
videoWriter = cv2.VideoWriter(video_path,fourcc,fps,(W,H))

for index,name in enumerate(img_list):
    print(index)
    frame = cv2.resize(cv2.imread(name),(W,H))
    videoWriter.write(frame)

videoWriter.release()
print("finish")


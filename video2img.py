#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/27 14:39 
# @Software: PyCharm
# @Author : wzg16
"""
@File : video2img.py
@Function:

"""
import cv2
import os


def video2img(video_path, frame_save_dir):
    cap = cv2.VideoCapture(video_path)
    suc = cap.isOpened()
    frame_count = 0
    while suc:
        suc, frame = cap.read()  # suc是bool变量，用于判断视频帧是否存在
        frame_count += 1
        if suc:
            save_path = os.path.join(frame_save_dir, "{:04d}.jpg".format(frame_count))  # 格式化命名，不足补零
            cv2.imwrite(save_path, frame)
            print(frame_count, suc)
    cap.release()


if __name__ == "__main__":
    video_path = "./01_001.avi"
    frame_save_dir = "./frames"  # 需要预先创立该文件夹
    video2img(video_path, frame_save_dir)

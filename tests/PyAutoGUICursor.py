# -*- coding: utf-8 -*-

# Python Random String Password
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/t/python/13398

import time

import pyautogui

while True:
    # 移动鼠标，duration=0.1是鼠标移动过程中的延迟速度
    pyautogui.moveTo(x=300, y=300, duration=0.1)
    time.sleep(3)

    # 移动鼠标到坐标后，单击左键
    pyautogui.click(x=700, y=300, duration=0.1)
    time.sleep(3)

    # 移动鼠标到坐标后，双击左键
    pyautogui.doubleClick(x=600, y=300, duration=0.1)
    time.sleep(3)

    # 移动鼠标到坐标后，单击右键
    pyautogui.rightClick(x=700, y=300, duration=0.1)
    time.sleep(3)

    pyautogui.click(x=100, y=200)
    time.sleep(3)

    pyautogui.click(x=200, y=400)
    time.sleep(3)

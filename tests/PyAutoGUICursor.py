# -*- coding: utf-8 -*-

# Python Random String Password
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/t/python-pyautogui/13400

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
    time.sleep(10)

    pyautogui.click(x=200, y=400)
    time.sleep(10)

    # 可以在 Windows 中打开 Paint，然后执行下面的语句
    distance = 200
    while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)  # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)  # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up
    time.sleep(10)




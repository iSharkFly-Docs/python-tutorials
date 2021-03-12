# -*- coding: utf-8 -*-
# Python script to Process DateTime
# Author - HoneyMoose

import datetime

json_filename = 'resources/black_rock_test.json'

today = datetime.date.today()
print("Today's date:", today)

# 从字符串创建日期对象
date_user = datetime.datetime.strptime('1/1/2021', '%m/%d/%Y')
print("格式化后的日期对象：", date_user)

# 日期对象通过对格式化输出
print("日期对象格式化输出 1 =", today.strftime("%d/%m/%Y"))
print("日期对象格式化输出 2 =", today.strftime("%B %d, %Y"))
print("日期对象格式化输出 3 =", today.strftime("%m/%d/%y"))
print("日期对象格式化输出 4 =", today.strftime("%b-%d-%Y"))

# 当前时间戳
now = datetime.datetime.now()
print("当前时间戳:", now)

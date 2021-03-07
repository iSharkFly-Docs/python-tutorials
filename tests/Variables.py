# -*- coding: utf-8 -*-

# Python 程序的变量（variables）定义
# Version: 0.1
# Author: YuCheng Hu

# 创建变量和指定变量类型
x = 1  # 变量赋值定义一个变量x
print(id(x))  # 打印变量x的标识
print(x + 1)  # 使用变量

x = 2  # 量赋值定义一个变量x
print(id(x))  # 此时的变量x已经是一个新的变量
print(x + 1)  # 名称相同，但是使用的是新的变量x

x = 4  # x 是整数类型的
x = "OSSEZ"  # x 类型将会修改为字符串
print(x)

print("==================")
x = 5
y = "John"
print(x)
print(y)

# 类型转换
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

# 获得类型
print("==================")
x = 5
y = "John"
print(type(x))
print(type(y))

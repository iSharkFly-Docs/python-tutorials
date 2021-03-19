# -*- coding: utf-8 -*-

# Python Random String Password
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/c/open-source/python/14

import string
from random import choice


def random_password(length, printable):
    """
    根据给定的字符串长度和可以用于生成字符串的字符集来生成随机字符串
    :param printable: 可用于生成随机字符串的字符
    :param int length: 生成随机字符串的数量
    """

    return "".join([choice(printable) for x in range(int(length))])


if __name__ == "__main__":
    3
    print(__name__)


amount = int(input("请输入需要生成随机字符串的数量: "))
number = int(input("请输入随机字符串的长度： "))

for i in range(1, amount + 1):
    print(f"   随机字符串 [Printable String]: {i} - {repr(random_password(number, string.printable))} ")

print('')
for i in range(1, amount + 1):
    print(f"   随机字符串 [Ascii Uppercase String]: {i} - {repr(random_password(number, string.ascii_uppercase))} ")

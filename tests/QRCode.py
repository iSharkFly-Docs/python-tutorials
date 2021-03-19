# -*- coding: utf-8 -*-

# Python QR Code Generator
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/c/open-source/python/14

import qrcode.image.svg

image_path = "resources/token_qr.png"

qr_string = "https://www.ossez.com/c/open-source/python/14"
print(qr_string)

img = qrcode.make(qr_string)
img.save(image_path)
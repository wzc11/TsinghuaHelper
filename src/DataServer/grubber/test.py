#!/usr/local/bin/python
#TODO: delete this file and debuger.py
#Usage : test.py username password
import sys
import glob
from PIL import Image

import debuger
ima = Image.open("test.jpg")
imb = ima.resize((243, 300))
a = Image.new("RGB", (540, 300), 'white')
a.paste(imb, (149, 0, 392, 300))
a.save('C:\\Users\\Public\\Pictures\\123.jpg')
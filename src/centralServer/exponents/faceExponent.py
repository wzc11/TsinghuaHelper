# -*- coding: utf-8 -*-
__author__ = 'YJB'

from PIL import Image


def faceExponent(src):
    im = Image.open(src.decode('UTF-8'))
    new_image = im.convert('L')
    sequence = new_image.getdata()
    data_num = 0.0
    average = 0.0
    for i in sequence:
        data_num = data_num + 1
        average += sequence[i]
    average /= data_num
    average -= 140
    average /= 2
    print(average)
    return average


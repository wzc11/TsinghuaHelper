# -*- coding: utf-8 -*-
__author__ = 'YJB'

import cStringIO, urllib2
from PIL import Image


def faceExponent(src):
    file = urllib2.urlopen(src)
    tmpIm = cStringIO.StringIO(file.read())
    im = Image.open(tmpIm)
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
    average = 30 - average
    if (average >= 10):
        average = 9.9
    if (average <= 0):
        average = 0.1
    print(average)
    return average


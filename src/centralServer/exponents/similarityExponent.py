# -*- coding: utf-8 -*-
__author__ = 'YJB'

import cStringIO, urllib2
import os
from PIL import Image

def similarityExponent(src1, src2):
    file1 = urllib2.urlopen(src1)
    tmpIm1 = cStringIO.StringIO(file1.read())
    image1 = Image.open(tmpIm1)
    #file2 = urllib2.urlopen(src2)
    #tmpIm2 = cStringIO.StringIO(file2.read())
    #image2 = Image.open(tmpIm2)
    #image1 = Image.open(src1.decode('UTF-8'))
    image2 = Image.open(src2.decode('UTF-8'))
    image1 = image1.resize((8, 8), Image.NEAREST).convert('1')
    image2 = image2.resize((8, 8), Image.NEAREST).convert('1')
    sequence1 = image1.getdata()
    sequence2 = image2.getdata()
    avg1 = reduce(lambda x, y: x + y, image1.getdata()) / 64.
    avg2 = reduce(lambda x, y: x + y, image2.getdata()) / 64.
    sequence1_result = []
    sequence2_result = []
    for i in range(0,64):
        if (sequence1[i] < avg1):
            sequence1_result.append(0)
        else:
            sequence1_result.append(1)
        if (sequence2[i] < avg2):
            sequence2_result.append(0)
        else:
            sequence2_result.append(1)
    sim = 0
    for i in range(0,64):
        if (sequence1_result[i] == sequence2_result[i]):
            sim = sim + 1
    return sim

def ListRoot(src1, rootDir):
     max = 0
     dir = ''
     fatherpath = os.getcwd()
     rootDir =  os.path.join(fatherpath, rootDir)
     rootDir.decode('UTF-8')
     for item in os.listdir(rootDir):
        path = os.path.join(rootDir, item)
        if (similarityExponent(src1, path) > max):
            max = similarityExponent(src1, path)
            dir = item
     max = max / 64.
     #print max
     return ['/static/img/picture/'+dir, max]

#ListRoot('C:\\Users\\JB\\Desktop\\软工图片\\12345.jpg', 'static\\img\\picture')
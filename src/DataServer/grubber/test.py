#!/usr/local/bin/python
#TODO: delete this file and debuger.py
#Usage : test.py username password
import sys

import debuger
from hunter_learn import hunter_learn


#print sys.argv[1], sys.argv[2]
h = hunter_learn(sys.argv[1], sys.argv[2])
l=h.getHomework("http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/hom_wk_detail.jsp?id=538195&course_id=103507&rec_id=null")
#l = h.getInfo()
debuger.printer(l)
#for course in l:
#    debuger.printer(h.getSpecial(course['id']))

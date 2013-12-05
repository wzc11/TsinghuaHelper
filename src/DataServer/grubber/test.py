#!/usr/local/bin/python
#TODO: delete this file and debuger.py
#Usage : test.py username password
import sys

import debuger
from hunter_learn import hunter_learn


print sys.argv[1], sys.argv[2]
h = hunter_learn(sys.argv[1], sys.argv[2])
l = h.getInfo()
#debuger.printer(l)
for course in l:
    debuger.printer(h.getSpecial(course['id'],[0]))

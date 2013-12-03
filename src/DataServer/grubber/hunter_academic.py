# -*- coding: utf-8 -*-
__author__ = 'WZC'
import cookielib
import urllib2
import urllib
import re
import datetime
import os
import socket
import time

from hunter import *


class userPassWrongException(Exception):
    def __init__(self, username):
        self.message = "Wrong Username({}) or Password.".format(username)


class hunter_academic(hunter):
    """This is the class hunter_academic,  a child of class hunter,
    to get full class table info (teacher, course caption, day & time, revenue, type, duration)
    from academic.tsinghua.edu.cn
    """
    infoRe_UnderGrad = re.compile(
        ur'''strHTML1 = "";\s*'''
        ur'''strHTML1 \+= ".(?P<teacher>[^"]*)";'''
        ur'''(\s*strHTML1 \+= ".(?P<type>[任选|限选|必修]*)";)?\s*'''
        ur'''strHTML1 \+= "；(?P<duration>[单周|全周|前八周]*)";\s*'''
        ur'''strHTML1 \+=".(?P<revenue>[^"]*)"([^"]|"[^>])*">(?P<caption>.*?)<[^\d]*(?P<time>\d*)_(?P<day>\d*)'''
    )
    infoRe_Graduate = re.compile(
        ur'''strHTML1 = "";\s*'''
        ur'''strHTML1 \+= "；(?P<teacher>[^"]*)";\s*'''
        ur'''strHTML1 \+= "；(?P<type>[学位课|非学位课|]*)";\s*'''
        ur'''strHTML1 \+= "；(?P<duration>[单周|全周|前八周]*)";\s*'''
        ur'''strHTML1 \+="；(?P<revenue>[^"]*)"\s*'''
        ur'''[\s\S]*?">(?P<caption>[^<]*)</span>'''
        ur'''[^\d]*(?P<time>\d*)_(?P<day>\d*)'''
    )
 
    basicInfoRe = re.compile(
        ur'''当前用户：\s*</span></td><td valign="middle" align="center"><span class="uportal-navi-user">(?P<real_name>.*?)</span></td>'''
        ur'''<td><img[^>]*></td><td valign="middle" align="center"><span class="uportal-navi-user">(?P<user_name>.*?)</span></td>'''
        ur'''<td><img[^>]*></td><td valign="middle" align="center"><span class="uportal-navi-user">(?P<student_number>\d*)</span></td></tr></table></td><td>'''
        #ur'''height="24" width="10" src=".*?"></td><td>(?P<student_number>\d+)<.*?>(?P<real_name>.*?)</td>'''
    )
    personReInfo = re.compile(
        ur'''<td align="left" bgcolor="#F2F2F2" class="hui"[^>]*>\s*(?P<info>[^<]*)'''
    )
    personReTitle = re.compile(
        ur'''bgcolor="#DFDFDF"\s*class="copyright">\s*(?P<title>[^<]*)'''
    )
    # TODO: check InfoRe for Graduate Student

    def login(self, username, password):
        """This is the login function
        Usage : login(self, username, password)
        Return : None
        """
        self.isGraduate = False
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj), urllib2.HTTPHandler)
        self.postdata = urllib.urlencode({
            'userName': username,
            'password': password,
            'x': '0',
            'y': '0'
        })
        self.header_sets = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'portal.tsinghua.edu.cn',
            'Origin': 'http://portal.tsinghua.edu.cn',
            'Referer': 'http://portal.tsinghua.edu.cn/index.jsp',
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'
        }
        self.req = urllib2.Request(
            url='https://portal.tsinghua.edu.cn/Login',
            data=self.postdata,
            headers=self.header_sets
        )
        self.cache = self.opener.open(self.req).read().decode('gb2312', 'ignore')
        if u'alert' in self.cache:
            raise userPassWrongException(username=username)
        self.cache = self.open('http://portal.tsinghua.edu.cn/render.userLayoutRootNode.uP').decode('utf-8', 'ignore')
        self.basicInfo = self.getMessageC(self.cache, self.basicInfoRe)[0]
        self.scorePreparation = False
        #file_object = open('test.txt', 'w+')
        #file_object.write((self.cache).encode('utf-8'))
        #file_object.close()

    def pseudoLogin(self, username, password):
        ftmp = open(os.path.abspath(os.path.dirname(__file__)) + "/academic_sample_basic.html", "r")
        content = ftmp.read().decode('utf-8')
        ftmp.close()
        #print content
        self.basicInfo = self.getMessageC(content, self.basicInfoRe)[0]

    def getBasicInfo(self):
        tmpDict = {}
        tmpDict.update(self.basicInfo)
        return tmpDict

    def logout(self):
        self.header_sets = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.6',
            'Connection': 'keep-alive',
            'Host': 'academic.tsinghua.edu.cn',
            'Referer': 'http://academic.tsinghua.edu.cn/render.userLayoutRootNode.uP',
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
        }
        #self.req = urllib2.Request(
        #    url='http://portal.tsinghua.edu.cn/Logout',
        #    headers=self.header_sets
        #)
        self.open('http://portal.tsinghua.edu.cn/Logout')


    def specialfunc(self, listdata):
        for i in listdata:
            if i['teacher'] in (u'限选', u'任选', u'必修', u'学位课', u'非学位课'):
                i['type'] = i['teacher']
                i['teacher'] = 'unknown'
            if not i['type']:
                i['type'] = u'体育'
        return listdata

    # This function will get all courses' id & name
    def getCourseInfo(self):

if __name__ == "__main__":
    import sys
    import debuger
    h = hunter_academic(sys.argv[1], sys.argv[2])
    #debuger.printer(h.getPersonInfo(),'gbk')
    debuger.printer(h.getCourseInfo())


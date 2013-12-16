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
import random
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
        ur'''当前用户：\s*</span></td><td valign="middle" align="center"><span class="uportal-navi-user">\s*(?P<real_name>.*?)\s*</span></td>'''
        ur'''<td><img[^>]*></td><td valign="middle" align="center"><span class="uportal-navi-user">\s*(?P<user_name>.*?)\s*</span></td>'''
        ur'''<td><img[^>]*></td><td valign="middle" align="center"><span class="uportal-navi-user">\s*(?P<student_number>\d*)\s*</span></td></tr></table></td><td>'''
    )
    personReInfo = re.compile(
        ur'''align="left" bgcolor="" >\s*(?P<info>[^<]*)\s*</'''
    )
    personReTitle = re.compile(
        ur'''<div align="right">\s*(?P<title>[^<]*)\s*</div>'''
    )

    def login(self, username, password):
        """This is the login function
        Usage : login(self, username, password)
        Return : None
        """
        self.isGraduate = False
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj), urllib2.HTTPHandler)
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        self.postdata = urllib.urlencode({
            'userName': username,
            'password': password,
            'x': x,
            'y': y
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
        self.open('http://portal.tsinghua.edu.cn/Logout')


    def specialfunc(self, listdata):
        for i in listdata:
            if i['teacher'] in (u'限选', u'任选', u'必修', u'学位课', u'非学位课'):
                i['type'] = i['teacher']
                i['teacher'] = 'unknown'
            if not i['type']:
                i['type'] = u'体育'
        return listdata


    def getCourseInfo(self):
        """This is the getinfo function,
        which returns a list of dicts with 7 keys
        (teacher, caption, day, time, revenue, type, duration)
        """
        if self.useBuffer:
            fAcaBuf = open(os.path.abspath(os.path.dirname(__file__)) + "/academic_sample.html", "r")
            try:
                self.content = fAcaBuf.read().decode('utf-8', 'r')
            finally:
                fAcaBuf.close()

            result = self.specialfunc(self.getMessageC(self.content, self.infoRe_UnderGrad))
            if not result:
                self.tnow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            return result
        else:
            self.urlre = re.compile(
                r'''http://zhjw.cic.tsinghua.edu.cn/j_acegi_login.do\?url=/jxmh.do&amp;m=bks_yjkbSearch&amp;ticket=\w*''')
            self.urlre2 = re.compile(
                r'''http://zhjw.cic.tsinghua.edu.cn/j_acegi_login.do\?url=/jxmh.do&amp;m=yjs_kbSearch&amp;ticket=\w*''')
            self.refreshCache()
            res = self.urlre.search(self.cache)
            if res:
                self.target_url = res.group().replace("amp;", "")
            else:
                self.isGraduate = True
                self.target_url = self.urlre2.search(self.cache).group().replace("amp;", "")
            self.content = self.opener.open(self.target_url).read().decode('gbk', 'ignore')

            if self.isGraduate:
                result = self.getMessageC(self.content, self.infoRe_Graduate)
            else:
                result = self.specialfunc(self.getMessageC(self.content, self.infoRe_UnderGrad))
            if not result:
                self.tnow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            return result


    def refreshCache(self):
        self.cache = self.open('http://portal.tsinghua.edu.cn/render.userLayoutRootNode.uP').decode('utf-8', 'ignore')

   
    def getPersonInfo(self, image_name):

        def dealReplace(content):
            return content.replace('&nbsp;', ' ')

        def dealClear(content):
            return content.strip(' \n\t\r')

        self.refreshCache()
        self.urlre = re.compile(
                r'''http://zhjw.cic.tsinghua.edu.cn/j_acegi_login.do\?url=/jxmh.do&amp;m=bks_yxkccj&amp;ticket=\w*''')
        res = self.urlre.search(self.cache)
        self.target_url = res.group().replace("amp;", "")

        self.opener.open(self.target_url)
        self.header_sets_img = {
            'Host': 'zhjw.cic.tsinghua.edu.cn',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.6',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
        }
        dict = {}
        title = self.getMessage('http://zhjw.cic.tsinghua.edu.cn/jxmh.do?m=bks_ShowBksXx', self.personReTitle, 'gbk', dealReplace)
        info = self.getMessage('http://zhjw.cic.tsinghua.edu.cn/jxmh.do?m=bks_ShowBksXx', self.personReInfo, 'gbk', dealReplace)
        if (len(info) == 0):
            return []
        for i in range(len(info)):
            dict[dealClear(title[i]['title'])[:-1]] = dealClear(info[i]['info'])
        self.req_img = urllib2.Request(
            url = 'http://zhjw.cic.tsinghua.edu.cn/xsBks.xsBksXjb.do?m=down&p_id='+dealClear(info[0]['info']),
            headers=self.header_sets_img,
        )
        socket = self.opener.open(self.req_img)
        data = socket.read()
        socket.close()
        img = open('C:\\Users\\ziyewuge\\Pictures\\TsinghuaHelper\\old\\' + image_name + '.jpg', 'wb')
        img.write(data)
        img.close()
        return [dict, data]

if __name__ == "__main__":
    import sys
    import debuger
    h = hunter_academic('caoy11', 'memory2011')
    debuger.printer(h.getBasicInfo())
    debuger.printer(h.getCourseInfo())
    debuger.printer(h.getPersonInfo('123123')[0])

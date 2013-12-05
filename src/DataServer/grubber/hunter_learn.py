# -*- coding: utf-8 -*-
__author__ = 'YJB'
import cookielib
import urllib2
import urllib
import re
import sys

from hunter import *


DEFAULT_HOST = "http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/"


class userPassWrongException(Exception):
    def __init__(self, message="Wrong Username or Password."):
        self.message = message


class connectionError(Exception):
    pass


class hunter_learn(hunter):
    ENUM_NOTICE, ENUM_CLASSINFO, ENUM_FILES, ENUM_HOMEWORK, ENUM_RESOURCES = range(5)
    infoRe = re.compile(
        ur'<a href="/MultiLanguage/lesson/student/course_locate\.jsp\?course_id=(?P<id>\d*)" target="_blank">\s*'
        ur'(?P<caption>.*?)\s*</a></td>\s*'
        ur'<td width="15%" ><span class="red_text">\s*(?P<homework>\d*)\s*</span>个未交作业</td>\s*'
        ur'<td width="15%" ><span class="red_text">\s*(?P<notice_unread>\d*)\s*</span>个未读公告</td>\s*'
        ur'<td width="15%" ><span class="red_text">\s*(?P<file_unread>\d*)\s*</span>个新文件</td>'
    )
    noticeRe = re.compile(
        r'''<a\s*href='(?P<link>[^']*)'>\s*(?P<caption>.*?)\s*</a>\s*'''
        r'''</td>\s*'''
        r'''<td width='15%'\s*align='center'\s*height=25>\s*(?P<teacher>.*?)\s*</td>\s*'''
        r'''<td width='20%'\s*align='center'\s*height=25>\s*(?P<date>.*?)\s*</td>\s*'''
    )
    classInfoRe = re.compile(
        ur'<td width="12%" height="25" class="tableTR1">姓名</td>\s*'
        ur'<td width="22%" class="tr_1">(?P<teacher_name>.*?)\s*</td>\s*'
        ur'<td class="tableTR1">电子邮件</td>\s*'
        ur'<td class="tr_1">\s*(?P<teacher_email>.*?)\s*</td>'
    )
    fileRe = re.compile(
        r'<a target="_top" href="(?P<link>.*?)" >\s*'
        r'\s*(?P<caption>.*?)\s*</a>\s*</td>'
        r'\s*<td width="300" align="center">\s*(?P<note>[\s\S]*?)\s*</td>\s*'
        r'<td width="80" align="center">\s*(?P<size>.*?)\s*</td>\s*'
        r'<td width="100" align="center">\s*(?P<date>.*?)\s*</td>'
    )
    homeworkRe = re.compile(
        r'<td width="30%"><a href="(?P<link>.*?)">\s*(?P<caption>.*?)\s*</a></td>\s*'
        r'<td width="10%">\s*(?P<date>.*?)\s*</td>\s*'
        r'<td width="10%">\s*(?P<deadline>.*?)\s*</td>\s*'
        r'<td width="15%" >\s*'
        r'(?P<state>.*?)\s*'
        r'</td>\s*'
        r'<td width="10%">\s*(?P<size>.*?)\s*'
        r'</td>\s*'
        r'<td width="25%">\s*'
        r'''<input id="submit_hw" name="submit_hw" value="[^"]*" (disabled="(?P<cannot_submit>[^"]*)")? type="button" onclick="[^"]*"\s*/>\s*'''
        r'''<input id="lookinfo" name="lookinfo" value="[^"]*" (disabled="(?P<cannot_see_review>[^"]*)")? type="button"  onclick="javascript:window.location.href='(?P<review_link>[^']*)'";\s*/>'''
    )
    homeworkDetailRe = re.compile(
        r'<td class="info_title"><img src="/img/info_title.gif" />\s*(?P<subject>.*?)\s*</td>\s*'
        r'</tr>\s*<tr>\s*<td class="info_x">\s*</td>\s*</tr>\s*<tr>\s*'
        r'<td colspan="3" valign="top">\s*'
        r'<table id="table_box" cellspacing="1" cellpadding="0">\s*'
        r'<tr>\s*'
        r'<td width="15%" height="25" class="title">.*?</td>\s*'
        r'<td class="tr_2">\s*(?P<caption>.*?)\s*</td>\s*'
        r'</tr>\s*<tr>\s*'
        r'<td height="100" class="title">.*?</td>\s*'
        r'<td class="tr_2">\s*<textarea cols=55  rows="7" style="width:650px"\s*'
        r'wrap=VIRTUAL>\s*(?P<note>[\s\S]*?)</textarea></td>\s*'
        r'</tr>\s*<tr>\s*'
        r'<td height="25" class="title">.*?</td>\s*'
        r'<td class="tr_2">&nbsp;\s*'
        r'(<a target="_top" href="(?P<file_link>[^"]*)">\s*(?P<file_name>.*?)\s*</a>)?[^<]*'
        r'</td>\s*</tr>\s*<tr>\s*<td height="5" colspan="2" class="lift">.*?</td>\s*'
        r'</tr>\s*<tr>\s*'
        r'<td height="100" class="title">.*?</td>\s*'
        r'<td class="tr_2"><textarea cols=55  rows="7" style="width:650px"  wrap=VIRTUAL>\s*(?P<submitted_note>[\s\S]*?)</textarea></td>\s*'
        r'</tr>\s*<tr>\s*<td height="25" class="title">.*?</td>\s*'
        r'<td class="tr_2">&nbsp;\s*'
        r'(<a target="_top" href="(?P<submitted_file_link>[^"]*)">\s*(?P<submitted_file_name>.*?)\s*</a>)?'
    )
    resRe = re.compile(
        r'<td width="35%" height="25">\s*'
        r'''<a onclick="[^"]*" href="(?P<link>[^"]*)" target="_blank">\s*'''
        r'(?P<caption>.*?)\s*</a>\s*'
        r'</td>\s*'
        r'<td width="65%">\s*(?P<note>[\s\S]*?)\s*</td>'
    )
    personRe = [
        re.compile(
            r'name\s*size=40\s*value="(?P<name>[^"]*)"'
        ),
        re.compile(
            r'email\s*size=40\s*value="(?P<email>[^"]*)"\s*maxlength="40"'
        ),
        re.compile(
            r'gender\s*value="(?P<gender>[^"]*)"'
        ),
        re.compile(
            r'user_type\s*value="(?P<user_type>[^"]*)"'
        )
    ]

    def login(self, username, password):
        self.TimeMachine = 1
        self.cj = cookielib.CookieJar()
        self.cookie_support = urllib2.HTTPCookieProcessor(self.cj)
        self.opener = urllib2.build_opener(self.cookie_support, urllib2.HTTPHandler)

        self.postdata = urllib.urlencode({
            'userid': username,
            'userpass': password,
            'submit1': '%B5%C7%C2%BC'
        })
        self.header_sets = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.6',
            'ache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'learn.tsinghua.edu.cn',
            'Origin': 'http://learn.tsinghua.edu.cn',
            'Referer': 'http://learn.tsinghua.edu.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'
        }

        self.req = urllib2.Request(
            url='https://learn.tsinghua.edu.cn/MultiLanguage/lesson/teacher/loginteacher.jsp',
            data=self.postdata,
            headers=self.header_sets
        )
        result = self.opener.open(self.req).read().decode('utf-8', 'ignore')
        if result.find("alert") > 0:
            raise userPassWrongException

    def pseudoLogin(self, username, password):
        pass

    def logout(self):
        if ():
            self.header_sets = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.6',
                'Connection': 'keep-alive',
                'Host': 'learn.tsinghua.edu.cn',
                'Referer': 'http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/mainstudent.jsp',
                'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7'
            }
        self.req = urllib2.Request(
            url='http://learn.tsinghua.edu.cn/MultiLanguage/lesson/logout.jsp',
            headers=self.header_sets
        )
        self.opener.open(self.req)

    def datadeal(self, li, Host=DEFAULT_HOST):
        print li
        for i in li:
            for j in i:
                if i[j] is None:
                    i[j] = "Null"
                else:
                    if not 'note' in j:
                        i[j] = i[j].strip().replace("&nbsp;", " ")
                    if 'link' in j and ( not "http:" in i[j]):
                        i[j] = Host + urllib.quote(i[j].encode('utf-8', 'ignore'), ":?=/&%")
                i[j].strip(' \t')
        return li

    def getInfo(self):
        if self.TimeMachine == 1:
            return self.getMessage("http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/MyCourse.jsp?language=cn",
                                   self.infoRe, 'utf-8')
        else:
            return self.getMessage(
                "http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/MyCourse.jsp?typepage=" + str(
                    self.TimeMachine) + "&language=cn", self.infoRe, 'utf-8')

    def getSpecial(self, id, specification=[0, 1, 2, 3, 4]):
        self.data = dict()
        if self.ENUM_NOTICE in specification:
            self.data['notice'] = self.datadeal(self.getMessage(
                "http://learn.tsinghua.edu.cn/MultiLanguage/public/bbs/getnoteid_student.jsp?course_id=" + id,
                self.noticeRe, 'utf-8'), "http://learn.tsinghua.edu.cn/MultiLanguage/public/bbs/")
        if self.ENUM_CLASSINFO in specification:
            self.data['classinfo'] = self.datadeal(
                self.getMessage(DEFAULT_HOST + "course_info.jsp?course_id=" + id, self.classInfoRe, 'utf-8'))
        if self.ENUM_FILES in specification:
            self.data['files'] = self.datadeal(
                self.getMessage(DEFAULT_HOST + "download.jsp?course_id=" + id, self.fileRe, 'utf-8'),
                "http://learn.tsinghua.edu.cn")
        if self.ENUM_HOMEWORK in specification:
            self.data['homework'] = self.datadeal(
                self.getMessage(DEFAULT_HOST + "hom_wk_brw.jsp?course_id=" + id, self.homeworkRe, 'utf-8'))
        if self.ENUM_RESOURCES in specification:
            self.data['resources'] = self.datadeal(
                self.getMessage(DEFAULT_HOST + "ware_list.jsp?course_id=" + id, self.resRe, 'utf-8'), '')
        return self.data

    def getHomework(self, link):
        return self.datadeal(self.getMessage(link, self.homeworkDetailRe, 'gbk'), "http://learn.tsinghua.edu.cn")

    def getPersonal(self):
        self.data = dict()
        self.cache = self.open("http://learn.tsinghua.edu.cn/MultiLanguage/vspace/vspace_userinfo1.jsp").decode('utf-8', 'ignore')
        for r in self.personRe:
            self.listtmp = self.getMessageC(self.cache, r)
            if self.listtmp:
                self.data = dict(self.data.items() + self.listtmp[0].items())
        return self.data

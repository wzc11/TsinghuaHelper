__author__ = 'YJB'

import urllib2

def lazyDeal(content):
    return content

class hunter(object):
    #构造函数——完成login操作
    def __init__(self, username, password, useBuffer=False):
        self.useBuffer = useBuffer
        if not useBuffer:
            self.login(username, password)
        else:
            self.pseudoLogin(username, password)

    #析构函数——完成logout操作
    def __del__(self):
        if not self.useBuffer:
            self.logout()

    #获取HTML信息
    def open(self, turl):
        self.req = urllib2.Request(url=turl)
        return self.opener.open(self.req).read()

    #从content中截取有用的信息
    def getMessageC(self, content, r):
        self.ans = r.finditer(content)
        return [x.groupdict() for x in self.ans]

    #获取信息
    def getMessage(self, add, r, coding='utf-8', deal=lazyDeal):
        """Return a list of dict
        :type coding: list
        Usage: getMessage(address, Regular_Expr [, coding='utf-8' [, deal=lazyDeal ]])
        """
        self.cache2 = deal(self.open(add).decode(coding, 'ignore'))
        return self.getMessageC(self.cache2, r)
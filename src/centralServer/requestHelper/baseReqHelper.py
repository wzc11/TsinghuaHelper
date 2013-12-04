__author__ = 'wangzhuqi.THU'


import cookielib
import urllib2
import urllib
import json
import poster
import hashlib
import time
import re


class baseReqHelper(object):
    def __init__(self, email=None, password=None):
        if not email or not password:
            raise ValueError
        self._addHeaders()

        url_login = "https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN"
        m = hashlib.md5(password[0:16])
        m.digest()
        password = m.hexdigest()
        body = (('username', email), ('pwd', password), ('imgcode', ''), ('f', 'json'))
        try:
            msg = json.loads(self.opener.open(url_login, urllib.urlencode(body), timeout=5).read())
        except urllib2.URLError, e:
            print Exception, e
            raise weChatLoginException
        if msg['ErrCode'] not in (0, 65202):
            print msg
            raise weChatLoginException
        print "login:\t", msg
        self.token = msg['ErrMsg'].split('=')[-1]
        time.sleep(1)

    def _addHeaders(self):
        self.opener = poster.streaminghttp.register_openers()
        self.opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        self.opener.addheaders = [('Accept', 'application/json, text/javascript, */*; q=0.01'),
                                  ('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
                                  ('Referer', 'https://mp.weixin.qq.com/'),
                                  ('Cache-Control', 'max-age=0'),
                                  ('Connection', 'keep-alive'),
                                  ('Host', 'mp.weixin.qq.com'),
                                  ('Origin', 'mp.weixin.qq.com'),
                                  ('X-Requested-With', 'XMLHttpRequest'),
                                  ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                                 '(KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36')]

    def _sendMsg(self, sendTo, data):
        if isinstance(type(sendTo), type([])):
            for _sendTo in sendTo:
                self._sendMsg(_sendTo, data)
            return

        self.opener.addheaders += [('Referer', 'http://mp.weixin.qq.com/cgi-bin/singlemsgpage?fromfakeid={0}'
                                               '&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'.format(sendTo))]
        body = {
            'error': 'false',
            'token': self.token,
            'tofakeid': sendTo,
            'ajax': 1}
        body.update(data)
        print "body", body
        try:
            ret_json = json.loads(self.opener.open("https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&"
                                              "lang=zh_CN", urllib.urlencode(body), timeout=5).read())
            msg = ret_json['base_resp']['err_msg']
        except urllib2.URLError:
            time.sleep(1)
            return self._sendMsg(sendTo, data)
        print msg
        time.sleep(1)
        return msg

    def _getAppMsgId(self):
        msg = json.loads(self.opener.open(
            'http://mp.weixin.qq.com/cgi-bin/operate_appmsg?token={0}&lang=zh_CN&sub=list&'
            't=ajax-appmsgs-fileselect&type=10&pageIdx=0&'
            'pagesize=10&formid=file_from_{1}000&subtype=3'.format(
                self.token, int(time.time())),
            urllib.urlencode({'token': self.token,
                              'ajax': 1})).read())
        time.sleep(1)
        return msg['List'][0]['appId']

    def _getFakeId(self):
        msg_url = 'https://mp.weixin.qq.com/cgi-bin/message?t=message/list&count=1000&day=7' \
                  '&offset=0&token=' +\
                  self.token + '&lang=zh_CN'
        print self.opener.open(msg_url).read()


class weChatLoginException(Exception):
    pass
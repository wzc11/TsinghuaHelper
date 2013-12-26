__author__ = 'wangzhuqi.THU'
import time
import hashlib
from projectManager.CONFIG import *
from django.utils.encoding import smart_str
from xmlHelper.xmlHelper import *
from eventHandler import *
from textHandler import *


def checkSignature(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echoStr = request.GET.get('echostr', None)
    token = TOKEN

    checkList = [token, timestamp, nonce]
    checkList.sort()
    checkStr = "%s%s%s" % tuple(checkList)
    checkStr = hashlib.sha1(checkStr).hexdigest()
    if checkStr == signature:
        return echoStr
    else:
        return None


def autoResponder(request):
    rawStr = smart_str(request.body)
    data = xmlHelper.parse(rawStr)
    print data

    if data['content']['MsgType'] == 'text':
        reply = textHandler(data)
    elif data['content']['MsgType'] == 'event':
        reply = eventHandler(data)

    print 'REPLY:', reply
    try:
        if reply['type'] == 'TEXT_TEMPLATE':
            return xmlHelper.generate({
                'to': data['content']['FromUserName'],
                'from': data['content']['ToUserName'],
                'time': str(int(time.time())),
                'content': reply['data']['content']
            }, XML['TEXT_TEMPLATE'])['content']
        elif reply['type'] == 'IMAGE_TEXT_TEMPLATE':
            return xmlHelper.generate({
                'to': data['content']['FromUserName'],
                'from': data['content']['ToUserName'],
                'time': str(int(time.time())),
                'count': reply['data']['count'],
                'template-child': reply['data']['template-child'],
            }, XML['IMAGE_TEXT_TEMPLATE'])['content']
        else:
            return xmlHelper.generate({
                'to': data['content']['FromUserName'],
                'from': data['content']['ToUserName'],
                'time': str(int(time.time())),
                'title': reply['data']['title'],
                'description': reply['data']['content'],
                'picUrl': reply['data']['url'],
                'link': reply['data']['link'],
            }, XML['USER_INFO_TEMPLATE'])['content']
    except Exception, e:
        print Exception, e
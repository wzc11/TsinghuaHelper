__author__ = 'wangzhuqi.THU'

import time
import hashlib
import urllib2
import json
from django.utils.encoding import smart_str
from xmlHelper.xmlHelper import *
from config import *


weChatXMLHelper = xmlHelper(config_xml)


def checkSignature(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echoStr = request.GET.get('echostr', None)
    token = config_token

    checkList = [token, timestamp, nonce]
    checkList.sort()
    checkStr = "%s%s%s" % tuple(checkList)
    checkStr = hashlib.sha1(checkStr).hexdigest()
    if checkStr == signature:
        return echoStr
    else:
        return None


def responseMsg(request):
    rawStr = smart_str(request.body)
    msg = xmlHelper.parse(rawStr)

    replyContent = {
        'to': msg['content']['FromUserName'],
        'from': msg['content']['ToUserName'],
        'time': str(int(time.time())),
        'type': 'text',
        'content': msgForward(config_url['retrieval'], msg)
    }
    return weChatXMLHelper.generate(replyContent)['content']


def msgForward(url, msg):
    fwdData = parseFunc(msg)
    print fwdData
    if fwdData['type'] == 'err':
        return 'err: unknown query item'
    data = json.dumps(fwdData)
    request = urllib2.Request(url, data)
    try:
        response = urllib2.urlopen(request)
        recv = json.loads(response.read())
        print recv
        if recv['error'] == 0:
            reply = ''
            for item in recv['data']:
                reply += item.encode('utf-8')
                reply += '\n'
        else:
            reply = 'err: ', recv['data']
    except Exception, e:
        reply = Exception, e
        print Exception, e

    return reply


def parseFunc(data):
    fwdData = {
        'type': '',
        'data': {
            'type': 0,
            'user_id': data['content']['FromUserName'],
            'username': '',
            'password': '',
            'course_caption': '',
            'homework_caption': '',
            'notice_caption': '',
            'files_caption': ''
        }
    }

    fwdStr = data['content']['Content']

    list = fwdStr.split('#')
    index = 0

    for rawStr in list:
        list[index] = rawStr.strip()
        index += 1

    if list[0] == '1':
        fwdData['type'] = 'bind'
        fwdData['data']['username'] = list[1]
        fwdData['data']['password'] = list[2]
    elif list[0] == '2':
        fwdData['type'] = 'course_list'
    elif list[0] == '3':
        fwdData['type'] = 'course_info'
        fwdData['data']['course_caption'] = list[1]
    elif list[0] == '4':
        fwdData['type'] = 'homework_list'
        fwdData['data']['course_caption'] = list[1]
    elif list[0] == '5':
        fwdData['type'] = 'homework_info'
        fwdData['data']['course_caption'] = list[1]
        fwdData['data']['homework_caption'] = list[2]
    elif list[0] == '6':
        fwdData['type'] = 'notice_list'
        fwdData['data']['course_caption'] = list[1]
    elif list[0] == '7':
        fwdData['type'] = 'notice_info'
        fwdData['data']['course_caption'] = list[1]
        fwdData['data']['notice_caption'] = list[2]
    elif list[0] == '8':
        fwdData['type'] = 'files_list'
        fwdData['data']['course_caption'] = list[1]
    elif list[0] == '9':
        fwdData['type'] = 'files_info'
        fwdData['data']['course_caption'] = list[1]
        fwdData['data']['files_caption'] = list[2]
    else:
        fwdData['type'] = 'err'

    return fwdData
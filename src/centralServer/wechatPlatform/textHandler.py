__author__ = 'wangzhuqi.THU'
# -*- coding: utf-8 -*-
from requestHelper.forwardHelper import *
from projectManager.CONFIG import *
from requestHelper.messageHelper import *


def textHandler(data):
    code = data['content']['Content']
    fakeId = weChatUtil.Authorize(code)
    reply = {
        'data': {
            'content': '验证成功',
        },
        'type': 'TEXT_TEMPLATE',
    }


    fwdData = {
        'type': data['content']['EventKey'],
        'data': {
            'user_id': data['content']['FromUserName'],
            'fake_id': fakeId,
        }
    }

    retData = forwardRequest(URL['DATA'], fwdData)

    return reply
'''def textHandler(data):
    argMap = textParser(data['content'])
    fwdData = {
        'type': '',
        'data': {
            'user_id': data['content']['FromUserName'],
            'username': '',
            'password': '',
            'course_caption': '',
            'homework_caption': '',
            'notice_caption': '',
            'files_caption': ''
        }
    }

    retData = forwardRequest(URL['DATA'], fwdData)
    print retData

    if retData['type'] == 'ERR':
        reply = 'ERR:\n'
        for item in retData['data']:
                reply += item.encode('utf-8')
                reply += '\n'
    elif retData['type'] == 'TEXT':
        reply = ''
        for item in retData['data']:
                reply += item.encode('utf-8')
                reply += '\n'
    elif retData['type'] == 'IMAGE_TEXT':
        reply = ''
        for item in retData['data']:
                reply += item.encode('utf-8')
                reply += '\n'
    else:
        reply = 'WRONG CODE'

    return reply


def textParser(text):
    argMap = {}

    return argMap'''
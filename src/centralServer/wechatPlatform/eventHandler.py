# -*- coding: utf-8 -*-
__author__ = 'wangzhuqi.THU'
from requestHelper.forwardHelper import *
from projectManager.CONFIG import *


def eventHandler(data):
    fwdData = {
        'type': data['content']['EventKey'],
        'data': {
            'user_id': data['content']['FromUserName']
        }
    }

    if fwdData['type'] == 'bind':
        return {
            'data': {
                'content': '请点击如下链接<a href="http://thusecretary.duapp.com/weChat/login/?id='
                           + data['content']['FromUserName']
                           + '">绑定账号</a>',
            },
            'type': 'TEXT_TEMPLATE',
        }

    retData = forwardRequest(URL['DATA'], fwdData)

    reply = {
        'data': {},
        'type': 'TEXT_TEMPLATE',
    }
    if retData['error'] == 1:
        reply['data']['content'] = 'ERR:\n'
        for item in retData['data']:
                reply['data']['content'] += item.encode('utf-8')
                reply['data']['content'] += '\n'
    elif retData['error'] == 0:
        if data['content']['EventKey'] == 'user_info':
            reply['type'] = 'USER_INFO_TEMPLATE'
            reply['data']['url'] = retData['url'].encode('utf-8')
        reply['data']['content'] = ''
        for item in retData['data']:
                reply['data']['content'] += item.encode('utf-8')
                reply['data']['content'] += '\n'
        reply['data']['content'] += '点击可查看具体信息'
        print 're test:', reply
    else:
        reply['data']['content'] = 'WRONG CODE'

    return reply
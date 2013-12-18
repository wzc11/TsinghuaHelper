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

    if fwdData['type'] == 'index':
        retData = forwardRequest(URL['DATA'], fwdData)

        print retData
        return {
            'data': {
                'content': '<a href="http://thusecretary.duapp.com/weChat/index/face/?src='
                           + retData['data'][2].encode('utf-8')
                           + '&name='
                           + retData['data'][0].encode('utf-8')
                           + '">屌丝指数</a>'
                           + '<a href="http://thusecretary.duapp.com/weChat/index/learn/?num='
                           + retData['data'][1].encode('utf-8')
                           + '&name='
                           + retData['data'][0].encode('utf-8')
                           + '&src='
                           + retData['data'][2].encode('utf-8')
                           + '">学霸指数</a>'
                           + '<a href="http://thusecretary.duapp.com/weChat/index/facePK/?src='
                           + retData['data'][2].encode('utf-8')
                           + '&name='
                           + retData['data'][0].encode('utf-8')
                           + '">明星脸</a>',
            },
            'type': 'TEXT_TEMPLATE',
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

    if fwdData['type'] == 'focus':
        return {
            'data': {
                'content': '请点击如下链接<a href="http://thusecretary.duapp.com/weChat/focus/?id='
                           + data['content']['FromUserName']
                           + '&fwd=false'
                           + '">选择关注课程</a>',
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
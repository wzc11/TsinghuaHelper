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

    if fwdData['type'] == 'unbind':
        return {
            'data': {
                'content': "已经解除绑定"
            },
            'type': 'TEXT_TEMPLATE'
        }

    if fwdData['type'] == 'card':
        return {
            'data': {
                'content': '<a href="'+URL['ROOT']+'card/?id='
                           + data['content']['FromUserName']
                           + '">个人名片</a>',
            },
            'type': 'TEXT_TEMPLATE',
        }

    if fwdData['type'] == 'index':
        return {
            'data': {
                'content': '<a href="'+URL['ROOT']+'index/face/?id='
                           + data['content']['FromUserName']
                           + '">屌丝指数</a>' + '\n'
                           + '<a href="'+URL['ROOT']+'index/learn/?id='
                           + data['content']['FromUserName']
                           + '">学霸指数</a>' + '\n'
                           + '<a href="'+URL['ROOT']+'index/facePK/?id='
                           + data['content']['FromUserName']
                           + '">明星脸</a>',
            },
            'type': 'TEXT_TEMPLATE',
        }

    if fwdData['type'] == 'bind':
        return {
            'data': {
                'content': '请点击如下链接<a href="'+URL['ROOT']+'login/?id='
                           + data['content']['FromUserName']
                           + '">绑定账号</a>',
            },
            'type': 'TEXT_TEMPLATE',
        }

    if fwdData['type'] == 'focus':
        return {
            'data': {
                'content': '请点击如下链接<a href="'+URL['ROOT']+'focus/?id='
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
        reply['data']['content'] = '数据正在获取中，请稍候...'

    return reply
__author__ = 'wangzhuqi.THU'
# -*- coding: utf-8 -*-
from requestHelper.forwardHelper import *
from projectManager.CONFIG import *
from requestHelper.messageHelper import *


def textHandler(data):
    openId = data['content']['FromUserName']
    code = data['content']['Content']
    '''try:'''
    fakeId = weChatUtil.Authorize(code)
    reply = {
        'data': {
            'content': '验证成功，正在获取数据，请稍候...',
        },
        'type': 'TEXT_TEMPLATE',
    }

    fwdData = {
        'type': 'fakeId',
        'data': {
            'user_id': openId,
            'fake_id': fakeId,
            #'username': APP_INFO_CACHE[openId]['usr'],
            #'password': APP_INFO_CACHE[openId]['pwd'],
        }
    }

    retData = forwardRequest(URL['DATA'], fwdData)
    #if retData['error'] == 0:
        #del(APP_INFO_CACHE[openId])
        #print APP_INFO_CACHE
    if retData['error'] != 0:
        print 'RETDATA', retData
        reply['data']['content'] = 'Error 验证码失效，请重新绑定'
    '''except Exception, e:
        reply = {
            'data': {
                'content': Exception + e,
            },
            'type': 'TEXT_TEMPLATE',
        }'''

    return reply
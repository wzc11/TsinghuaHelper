__author__ = 'wangzhuqi.THU'
# -*- coding: utf-8 -*-
from requestHelper.forwardHelper import *
from keyHandler.keyHandler import *
from eventHandler import *
from projectManager.CONFIG import *
from requestHelper.messageHelper import *


def textHandler(data):
    openId = data['content']['FromUserName']
    code = data['content']['Content']
    if code.isdigit():
        '''try:'''
        fakeId = weChatUtil.Authorize(code)
        reply = {
            'data': {
                'content': '正在获取数据，稍后通知您，请稍候...',
            },
            'type': 'TEXT_TEMPLATE',
        }

        fwdData = {
            'type': 'fakeId',
            'data': {
                'user_id': openId,
                'fake_id': fakeId,
                'test': code,
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
            reply['data']['content'] = errorHandler(retData['error'], openId)
        return reply
    else:
        try:
            data = {
                'content': {
                    'EventKey': keyHandler(code)
                }
            }
            return eventHandler(data)
        except Exception, e:
            return {
                'data': {
                    'content': '对不起,我们没有提供此关键字',
                },
                'type': 'TEXT_TEMPLATE',
            }
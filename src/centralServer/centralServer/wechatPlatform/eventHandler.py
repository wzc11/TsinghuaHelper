# -*- coding: utf-8 -*-
__author__ = 'wangzhuqi.THU'
from errorHandler import *
from requestHelper.forwardHelper import *
from validationHelper import *
from exponents.vcard import *


def eventHandler(data):
    fwdData = {
        'type': data['content']['EventKey'],
        'data': {
            'user_id': data['content']['FromUserName']
        }
    }

    if fwdData['type'] == 'subscribe':
        fwdData['type'] = 'unbind'
        forwardRequest(URL['DATA'], fwdData)
        deleteCard({
            'openId': data['content']['FromUserName'],
        })
        return {
            'data': {
                'content': '谢谢使用'
            },
            'type': 'TEXT_TEMPLATE'
        }

    if fwdData['type'] == 'card':
        retData = forwardRequest(URL['DATA'], fwdData)
        url = retrieveCard({
            'openId': data['content']['FromUserName'],
            'name': retData['data'][0],
            'major': retData['data'][4],
            'phone': retData['data'][1],
            'email': retData['data'][5],
        })
        return {
            'data': {
                'content': '',
                'title': '个人名片',
                'url': url[0],
                'link': url[1],
            },
            'type': 'INDEX_TEMPLATE',
        }

    if fwdData['type'] == 'faceIndex':
        validation = validationHelper(data['content']['FromUserName'])
        if validation != 'ok':
            return {
                'data': {
                    'content': validation
                },
                'type': 'TEXT_TEMPLATE'
            }
        return {
            'data': {
                'content': '',
                'title': '屌丝指数',
                'url': URL['ROOT']+'../static/img/diaosipic/logo.jpg',
                'link': URL['ROOT']+'index/face/?id='+data['content']['FromUserName'],
            },
            'type': 'INDEX_TEMPLATE',
        }

    if fwdData['type'] == 'learnIndex':
        validation = validationHelper(data['content']['FromUserName'])
        if validation != 'ok':
            return {
                'data': {
                    'content': validation
                },
                'type': 'TEXT_TEMPLATE'
            }
        return {
            'data': {
                'content': '',
                'title': '学霸指数',
                'url': URL['ROOT']+'../static/img/xuebapic/xuebalogo.jpg',
                'link': URL['ROOT']+'index/learn/?id='+data['content']['FromUserName'],
            },
            'type': 'INDEX_TEMPLATE',
        }

    if fwdData['type'] == 'facePK':
        validation = validationHelper(data['content']['FromUserName'])
        if validation != 'ok':
            return {
                'data': {
                    'content': validation
                },
                'type': 'TEXT_TEMPLATE'
            }
        return {
            'data': {
                'content': '',
                'title': '明星脸',
                'url': URL['ROOT']+'../static/img/facelogo-2.jpg',
                'link': URL['ROOT']+'index/facePK/?id='+data['content']['FromUserName'],
            },
            'type': 'INDEX_TEMPLATE',
        }

    if fwdData['type'] == 'aa':
        validation = validationHelper(data['content']['FromUserName'])
        if validation != 'ok':
            return {
                'data': {
                    'content': validation
                },
                'type': 'TEXT_TEMPLATE'
            }
        return {
            'data': {
                'content': '',
                'title': '明星脸',
                'url': URL['ROOT']+'../static/img/facelogo-2.jpg',
                'link': URL['ROOT']+'index/facePK/?id='+data['content']['FromUserName'],
            },
            'type': 'INDEX_TEMPLATE',
        }

    if fwdData['type'] == 'bind':
        validation = validationHelper(data['content']['FromUserName'], 'validation-bind')
        if validation != 'ok':
            return {
                'data': {
                    'content': validation
                },
                'type': 'TEXT_TEMPLATE'
            }
        return {
            'data': {
                'content': '请点击如下链接<a href="'+URL['ROOT']+'login/?id='
                           + data['content']['FromUserName']
                           + '">绑定账号</a>',
            },
            'type': 'TEXT_TEMPLATE',
        }

    if fwdData['type'] == 'deadline':
        validation = validationHelper(data['content']['FromUserName'], 'validation')
        if validation != 'ok':
            return {
                'data': {
                    'content': validation
                },
                'type': 'TEXT_TEMPLATE'
            }
        return {
            'data': {
                'content': '请点击如下链接<a href="'+URL['ROOT']+'calender/?id='
                           + data['content']['FromUserName']
                           + '">个人小秘书</a>',
            },
            'type': 'TEXT_TEMPLATE',
        }

    if fwdData['type'] == 'focus':
        validation = validationHelper(data['content']['FromUserName'])
        if validation != 'ok':
            return {
                'data': {
                    'content': validation
                },
                'type': 'TEXT_TEMPLATE'
            }
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
        'data': {
            'content': APP_EVENT[data['content']['EventKey']],
        },
        'type': 'TEXT_TEMPLATE',
    }

    if retData['error'] == 0:
        if data['content']['EventKey'] == 'score':
            reply['type'] = 'IMAGE_TEXT_TEMPLATE'
            reply['data']['count'] = str(retData['len']).encode('utf-8')
            reply['data']['template-child'] = {
                'templateXML': XML['ITEM_TEXT_TEMPLATE'],
                'collection': retData['data']
            }
            return reply
        if data['content']['EventKey'] == 'user_info':
            reply['type'] = 'USER_INFO_TEMPLATE'
            reply['data']['url'] = retData['url'].encode('utf-8')
            reply['data']['link'] = retData['link'].encode('utf-8')
            reply['data']['title'] = APP_EVENT[data['content']['EventKey']]
        for item in retData['data']:
            reply['data']['content'] += item.encode('utf-8')
            reply['data']['content'] += '\n\n'
        if data['content']['EventKey'] != 'unbind':
            reply['data']['content'] += '点击可查看具体信息'
        else:
            deleteCard({
                'openId': data['content']['FromUserName'],
            })
            reply['data']['content'] += '成功'
        print 're test:', reply
    else:
        reply['data']['content'] = errorHandler(retData['error'], data['content']['FromUserName'])

    return reply
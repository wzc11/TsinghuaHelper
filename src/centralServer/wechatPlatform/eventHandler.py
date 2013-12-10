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
        print 're test:', reply
    else:
        reply['data']['content'] = 'WRONG CODE'

    return reply
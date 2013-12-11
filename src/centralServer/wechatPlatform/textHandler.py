__author__ = 'wangzhuqi.THU'
from requestHelper.forwardHelper import *
from projectManager.CONFIG import *


def textHandler(data):
    return data['content']['Content']
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
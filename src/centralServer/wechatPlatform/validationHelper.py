__author__ = 'wangzhuqi.THU'
from requestHelper.forwardHelper import *
from projectManager.CONFIG import *
from errorHandler import *


def validationHelper(openId):
    retData = forwardRequest(URL['DATA'], {
        'type': 'validation',
        'data': {
            'user_id': openId,
        }
    })

    if retData['error'] == 0:
        return 'ok'
    else:
        return errorHandler(retData['error'], openId)
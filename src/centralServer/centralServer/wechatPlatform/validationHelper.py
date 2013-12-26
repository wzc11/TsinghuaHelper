__author__ = 'wangzhuqi.THU'
from requestHelper.forwardHelper import *
from projectManager.CONFIG import *
from errorHandler import *


def validationHelper(openId, type='validation'):
    retData = forwardRequest(URL['DATA'], {
        'type': type,
        'data': {
            'user_id': openId,
        }
    })

    if retData['error'] == 0:
        return 'ok'
    else:
        return errorHandler(retData['error'], openId)
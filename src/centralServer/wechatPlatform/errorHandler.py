# -*- coding: utf-8 -*-
__author__ = 'wangzhuqi.THU'
from projectManager.CONFIG import *


def errorHandler(errCode, openId):
    if errCode == 1:
        return '您尚未绑定账号,<a href="'\
               + URL['ROOT'] + 'login/?id='\
               + openId + '">绑定账号</a>'
    elif errCode == 2:
        return '服务器维护中...'
    elif errCode == 3:
        return '数据正在获取中，请稍候...'
    else:
        return '服务器错误...'
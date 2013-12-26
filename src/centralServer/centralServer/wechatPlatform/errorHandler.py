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
    elif errCode == 4:
        return '用户名密码错误'
    elif errCode == 5:
        return '您已经绑定'
    elif errCode == 6:
        return '验证码错误'
    elif errCode == -1:
        return '非法操作'
    else:
        return '服务器错误...'
# -*- coding: utf-8 -*-
__author__ = 'wangzhuqi.THU'
from requestHelper.reqHelper import reqHelper
from projectManager.CONFIG import *


weChatUtil = reqHelper(email=APP_ACCOUNT['email'], password=APP_ACCOUNT['password'])
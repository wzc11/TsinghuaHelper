# -*- coding: utf-8 -*-
__author__ = 'wangzhuqi.THU'
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
from requestHelper.reqHelper import reqHelper
from config import *
import json


weChatPlatform = reqHelper(email=config_reqHelper['email'], password=config_reqHelper['pass'])


@csrf_exempt
def weChatActiveHandler(request):
    if request.method == 'GET':
        return
    #try:
    #raw_str = smart_str(request.body)
    #raw_json = json.dumps(raw_str)
    #data = json.loads(raw_json)
    #print data
    #weChatPlatform.sentTextMsg("329239000", '尊敬的用户您好！您又多了10个大爹')
    weChatPlatform.Authorize(1)
    return HttpResponse("111")
    #except Exception, e:
    #    return Exception, e
# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from handler import *
from requestHelper.messageHelper import *
from django.template import RequestContext


@csrf_exempt
def weChatHandler(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
    elif request.method == 'POST':
        response = HttpResponse(autoResponder(request))
        return response
    else:
        return None


@csrf_exempt
def weChatLogin(request):
    try:
        openId = request.GET['id']
        print openId
    except Exception, e:
        openId = request.read()
        print Exception, e

    return render_to_response('login.html', {'openId': openId}, context_instance=RequestContext(request))


@csrf_exempt
def weChatFocus(request):
    try:
        fwdFlag = request.GET['fwd']
        openId = request.GET['id']
        print openId
    except Exception, e:
        fwdFlag = request.read()
        openId = request.read()
        print Exception, e
        return HttpResponse('找不到用户')

    fwdData = {
        'type': 'focus',
        'data': {
            'user_id': openId,
            'update_flag': fwdFlag,
            'update_data': {},
        }
    }

    if fwdData['data']['update_flag'] == 'true':
        newList = request.REQUEST.getlist('focusList')
        fwdData['data']['update_data'] = newList
        print fwdData

    retData = forwardRequest(URL['DATA'], fwdData)

    index = 0
    course_list = []
    for item in retData['data']:
        course_list.append({'content': item[0], 'checked': item[1], 'value': item[0]})
        index += 1

    print course_list
    return render_to_response('focus.html',
                              {'openId': openId, 'course_list': course_list},
                              context_instance=RequestContext(request))


@csrf_exempt
def weChatBind(request):
    usr = request.POST['uname']
    pwd = request.POST['pwd']
    openId = request.POST['openId']
    retData = forwardRequest(URL['DATA'], {
        'type': 'bind',
        'data': {
            'user_id': openId,
            'username': usr,
            'password': pwd,
        }
    })
    return HttpResponse(retData)


@csrf_exempt
def weChatMessage(request):
    #openId = request.POST['openId']
    #content = request.POST['openId']
    weChatUtil.sentTextMsg('110708680', '尊敬的用户您好，恭喜您获得菲尔兹一只')
    return HttpResponse('hahaha~')
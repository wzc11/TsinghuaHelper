# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from handler import *
from errorHandler import *
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
    print retData['data']
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
    if retData['error'] == 0:
        responseStr = '登陆成功，请回复验证码：'
        code = retData['test']
        #APP_INFO_CACHE[openId] = {'usr': usr, 'pwd': pwd}
        print APP_INFO_CACHE
    else:
        responseStr = errorHandler(retData['error'], openId)
        code = ''
    return render_to_response('yanzhengma.html',
                                {'str': responseStr, 'code': code},
                                context_instance=RequestContext(request))


@csrf_exempt
def weChatMessage(request):
    try:
        data = json.loads(smart_str(request.read()))
        print data
        weChatUtil.sentTextMsg(data['fake_id'].encode('utf-8'), data['result'].encode('utf-8'))
    except Exception, e:
        print Exception, e
    return HttpResponse('hahaha~')


@csrf_exempt
def weChatTest(request):
    code = request.GET['code']
    fakeId = weChatUtil.Authorize(code)
    return HttpResponse(fakeId)


@csrf_exempt
def weChatHelp(request):
    return render_to_response('help.html',{},
                        context_instance=RequestContext(request))
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from handler import *
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
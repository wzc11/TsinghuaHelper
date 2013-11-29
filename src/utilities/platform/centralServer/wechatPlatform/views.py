# Create your views here.
import time
import hashlib
import urllib
import urllib2
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
from xmlHelper.xmlHelper import *


weChatXML = {
    'template': """<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[%s]]></MsgType>
             <Content><![CDATA[%s]]></Content>
             <FuncFlag>0</FuncFlag>
             </xml>""",

    'data-tag': ['to', 'from', 'time', 'type', 'content']
}

weChatXMLHelper = xmlHelper(weChatXML)


def checkSignature(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echoStr = request.GET.get('echostr', None)
    token = 'ziyewuge'

    checkList = [token, timestamp, nonce]
    checkList.sort()
    checkStr = "%s%s%s" % tuple(checkList)
    checkStr = hashlib.sha1(checkStr).hexdigest()
    if checkStr == signature:
        return echoStr
    else:
        return None


def responseMsg(request):
    post = urllib2.Request(
        url='http://thusecretary.duapp.com/weixin/',
        headers={'Content-Type': 'application/xml', 'charset': 'UTF-8'},
        data=smart_str(request.body))
    receive = urllib2.urlopen(post)
    print receive
    return receive
    '''rawStr = smart_str(request.body)
    msg = xmlHelper.parse(rawStr)

    replyContent = {
        'to': msg['content']['FromUserName'],
        'from': msg['content']['ToUserName'],
        'time': str(int(time.time())),
        'type': 'text',
        'content': msg['content']['Content']
    }
    return weChatXMLHelper.generate(replyContent)['content']'''

def msgForward(url, content):
    data = urllib.urlencode(content)
    request = urllib2.Request(url, data)
    receive = urllib2.urlopen(request)
    print receive

@csrf_exempt
def handleRequest(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
    elif request.method == 'POST':
        response = HttpResponse(responseMsg(request))
        return response
    else:
        return None
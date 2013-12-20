__author__ = 'wangzhuqi.THU'
from django.shortcuts import render_to_response
from django.template import RequestContext
from exponents.faceExponent import *
from exponents.learnExponent import *
from exponents.similarityExponent import *
from requestHelper.forwardHelper import *
from projectManager.CONFIG import *


def weChatFaceIndex(request):
    openId = request.GET['id']
    fwdData = {
        'type': 'index',
        'data': {
            'user_id': openId
        }
    }

    retData = forwardRequest(URL['DATA'], fwdData)

    src = retData['data'][2]
    name = retData['data'][0]

    FacePoint = faceExponent(src)
    FacePoint = int(FacePoint / 2)
    if FacePoint == 0:
        FacePoint = 1
    return render_to_response('diaosi.html',
                              {'FacePoint': FacePoint, 'name': name, 'src': src},
                              context_instance=RequestContext(request))


def weChatLearnIndex(request):
    openId = request.GET['id']
    fwdData = {
        'type': 'index',
        'data': {
            'user_id': openId
        }
    }

    retData = forwardRequest(URL['DATA'], fwdData)

    src = retData['data'][2]
    name = retData['data'][0]
    num = retData['data'][1]

    sum = learnExponent(int(num), 0)
    sum = int(sum)
    if sum <= 0:
        sum = 1
    if sum >= 5:
        sum = 5
    return render_to_response('xueba.html',
                              {'Sum': sum, 'name': name, 'src': src},
                              context_instance=RequestContext(request))


def weChatPKIndex(request):
    openId = request.GET['id']
    fwdData = {
        'type': 'index',
        'data': {
            'user_id': openId
        }
    }

    retData = forwardRequest(URL['DATA'], fwdData)
    src = retData['data'][2]
    name = retData['data'][0]

    result = ListRoot(src, 'static\\img\\picture')

    return render_to_response('facepk.html',
                              {'url': result[0], 'name': name, 'sim': int(result[1]*100), 'src': src},
                              context_instance=RequestContext(request))


def weChatCard(request):
    openId = request.GET['id']
    fwdData = {
        'type': 'card',
        'data': {
            'user_id': openId
        }
    }

    retData = forwardRequest(URL['DATA'], fwdData)

    return render_to_response('person_card.html',
                              {'name': retData['data'][0],
                               'phone': retData['data'][1],
                               'id': retData['data'][2],
                               'birth': retData['data'][3],
                               'subject': retData['data'][4],
                               'email': retData['data'][5]},
                              context_instance=RequestContext(request))
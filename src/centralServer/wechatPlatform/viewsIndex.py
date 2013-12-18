__author__ = 'wangzhuqi.THU'
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from exponents.faceExponent import *
from exponents.learnExponent import *


def weChatFaceIndex(request):
    src = request.GET['src']
    name = request.GET['name']
    FacePoint = faceExponent(src)
    FacePoint = int(FacePoint / 2)
    if FacePoint == 0:
        FacePoint = 1
    return render_to_response('diaosi.html',
                              {'FacePoint': FacePoint, 'name': name},
                              context_instance=RequestContext(request))


def weChatLearnIndex(request):
    num = request.GET['num']
    credit = request.GET['credit']
    name = request.GET['name']
    sum = learnExponent(num, credit)
    sum = int(sum / 2)
    if sum == 0:
        sum = 1
    return render_to_response('xueba.html',
                              {'Sum': sum, 'name': name},
                              context_instance=RequestContext(request))
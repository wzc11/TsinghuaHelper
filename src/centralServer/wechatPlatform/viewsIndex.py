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
                              {'FacePoint': FacePoint, 'name': name, 'src': src},
                              context_instance=RequestContext(request))


def weChatLearnIndex(request):
    src = request.GET['src']
    num = request.GET['num']
    name = request.GET['name']
    sum = learnExponent(int(num), 0)
    sum = int(sum)
    if sum <= 0:
        sum = 1
    if sum >= 5:
        sum = 5
    return render_to_response('xueba.html',
                              {'Sum': sum, 'name': name, 'src': src},
                              context_instance=RequestContext(request))
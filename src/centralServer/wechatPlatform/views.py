# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from handlerFunc import *


@csrf_exempt
def weChatHandler(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
    elif request.method == 'POST':
        response = HttpResponse(responseMsg(request))
        return response
    else:
        return None
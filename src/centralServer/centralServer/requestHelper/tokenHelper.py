__author__ = 'wangzhuqi.THU'
from projectManager.CONFIG import *
import time
import json
import urllib2


def getToken():
    currentTime = int(time.time())
    if currentTime >= APP_TOKEN['refresh_time']:
        refreshToken(currentTime)
    return APP_TOKEN['access_token']


def refreshToken(currentTime):
    APP_TOKEN['refresh_time'] = currentTime + 6000
    try:
        response = urllib2.urlopen(URL['TOKEN'] % (APP_ID, APP_SECRET))
        data = json.loads(response.read())
        APP_TOKEN['access_token'] = data['access_token']
    except Exception, e:
        print Exception, e
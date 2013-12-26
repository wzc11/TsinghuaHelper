__author__ = 'wangzhuqi.THU'
import json
import urllib2


def forwardRequest(url, fwdData, format={'send': 'json', 'recv': 'json'}, headers=None, cookies=None):
    if format['send'] == 'json':
        data = json.dumps(fwdData)
    else:
        data = fwdData
    request = urllib2.Request(url, data)
    try:
        response = urllib2.urlopen(request)
        if format['recv'] == 'json':
            recvData = json.loads(response.read())
        else:
            recvData = response.read()
    except Exception, e:
        print Exception, e
        recvData = 'SERVER ERROR:', Exception, e

    return recvData
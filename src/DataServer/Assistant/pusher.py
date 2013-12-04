# -*- coding: utf-8 -*-
import json
import urllib2
__author__ = 'CaoYe'


class pusher(object):

    url = 'http://thusecretary.duapp.com/weChat/ActiveMsg/'

    def __init__(self, user_id):
        self.user_id = user_id

    def push(self, data_fwd):
        data = {
            'user_id': self.user_id,
            'content': data_fwd
        }
        request = urllib2.Request(self.url, json.dumps(data))
        try:
            response = urllib2.urlopen(request)
            data = json.loads(response.read())
            return True
        except:
            return False

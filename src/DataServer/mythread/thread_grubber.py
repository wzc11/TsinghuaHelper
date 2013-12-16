# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

import threading
from store.store_learn import *
from store.store_academic import *
from store.store_wechat import *
from Assistant.config import *
import json
import random


class thread_grubber(threading.Thread):
    def __init__(self, object):
        self.object = object

    def bind(self):
        result = 0
        store_learn_set = store_learn(self.object['username'], self.object['password'], self.object['user_id'])
        store_academic_set = store_academic(self.object['username'], self.object['password'], self.object['user_id'])
        if not store_learn_set.learn_store():
            result = 1
            return result
        if not store_academic_set.academic_store():
            result = 1
        return result

    def get_test(self):
        i = 0
        result = 0
        while i < 4:
            mid = random.randint(0, 9)
            result = result * 10 + mid
        return result

    def forwardRequest(self, url, fwdData):
        data = json.dumps(fwdData)
        request = urllib2.Request(url, data)
        try:
            response = urllib2.urlopen(request)
        except Exception, e:
            response = None
            print Exception, e
        return response

    def run(self):
        fwdData = {'test': self.get_test()}
        self.forwardRequest('thusecretary.duapp.com/weChat/message/', fwdData)
        bind_result = self.bind()
        fwdData = {
            'user_id': self.object['user_id'],
            'result': bind_result
        }
        fake_id = self.forwardRequest('thusecretary.duapp.com/weChat/message/', fwdData)
        store = store_wechat(self.object['username'], self.object['password'], self.object['user_id'])
        store.fake_id_store(fake_id)
        user_lock_list.remove(self.object['user_id'])



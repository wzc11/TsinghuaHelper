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
        threading.Thread.__init__(self)
        self.object = object

    def bind(self):
        result = '绑定成功，可以开始查询'.decode('UTF-8')
        store_learn_set = store_learn(self.object['username'], self.object['password'], self.object['user_id'])
        store_academic_set = store_academic(self.object['username'], self.object['password'], self.object['user_id'])
        if not store_learn_set.learn_store():
            result = '绑定失败,请重试'.decode('UTF-8')
            return result
        if not store_academic_set.academic_store():
            result = '绑定失败,请重试'.decode('UTF-8')
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
        bind_result = self.bind()
        fwdData = {
            'user_id': self.object['user_id'],
            'result': bind_result,
            'fake_id': self.object['fake_id']
        }
        print fwdData
        self.forwardRequest(connect_ip + 'message/', fwdData)
        store = store_wechat(self.object['username'], self.object['password'], self.object['user_id'])
        store.fake_id_store(self.object['fake_id'])
        user_lock_list.remove(self.object['user_id'])



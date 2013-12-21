__author__ = 'CaoYe'

# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

import threading
from store.store_learn import *
from store.store_academic import *
from store.store_wechat import *
from Assistant.config import *
from query.query_wechat import *
import json
import random


class thread_update(threading.Thread):
    def __init__(self, user_id):
        threading.Thread.__init__(self)
        self.user_id = user_id

    def update(self):
        result = '更新成功，可以开始查询'.decode('UTF-8')
        query = query_wechat(self.user_id)
        self.update_info = query.update_info_query()
        store_learn_set = store_learn(self.update_info[0], self.update_info[1], self.user_id)
        store_academic_set = store_academic(self.update_info[0], self.update_info[1], self.user_id)
        if not store_learn_set.learn_store():
            result = '更新失败,稍后重试'.decode('UTF-8')
            return result
        if not store_academic_set.academic_store():
            result = '更新失败,稍后重试'.decode('UTF-8')
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
        update_result = self.update()
        fwdData = {
            'user_id': self.user_id,
            'result': update_result,
            'fake_id': self.update_info[2]
        }
        print fwdData
        self.forwardRequest(connect_ip + 'message/', fwdData)
        user_lock_list.remove(self.user_id)
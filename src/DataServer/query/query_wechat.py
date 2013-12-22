# -*- coding: utf-8 -*-
__author__ = 'CaoYe'
from query import *


class query_wechat(query):
    def fake_id_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return None
        result = information['fake_id']
        return result

    def last_time_query(self):
        try:
            information = User.objects(user_id=self.user_id).next()
            result = information['last_time']
            return result
        except Exception, e:
            return 0

    def update_info_query(self):
        try:
            information = User.objects(user_id=self.user_id).next()
            result = [information['user_name'], information['use_password'], information['fake_id']]
            return result
        except Exception, e:
            return []

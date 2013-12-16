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
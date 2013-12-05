# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

from Assistant.docs import *
from grubber.hunter_learn import hunter_learn


class query(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def user_id_exist(self):
        try:
            test = User.objects(user_id=self.user_id).next()
            return True
        except Exception, e:
            return False

    def all_information_query(self):
        return User.objects(user_id=self.user_id)


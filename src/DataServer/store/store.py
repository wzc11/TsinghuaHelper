# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

from Assistant.docs import *
from grubber.hunter_learn import *
from grubber.hunter_academic import *


class store(object):

    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id

    def user_is_exist(self):
        user_list = User.objects(user_id=self.user_id)
        try:
            user_old = user_list.next()
            return True
        except Exception, e:
            return False

    def user_delete(self):
        user_list = User.objects(user_id=self.user_id)
        try:
            user_old = user_list.next()
            User.objects(user_id=self.user_id).delete()
        except Exception, e:
            return False
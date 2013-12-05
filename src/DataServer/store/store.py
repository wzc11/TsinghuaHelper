# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

from Assistant.docs import *
from grubber.hunter_learn import hunter_learn
from grubber.hunter_academic import hunter_academic


class store(object):

    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id

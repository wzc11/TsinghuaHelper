# -*- coding: utf-8 -*-
__author__ = 'CaoYe'
from store import *


class store_wechat(store):
    def fake_id_store(self, fake_id):
        User.objects(user_id=self.user_id).update(
            set__fake_id=fake_id
        )
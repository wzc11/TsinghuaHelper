# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

import docs
from hunter_learn import hunter_learn


class hunter_query:
    def __init__(self, username):
        self.username = username

    def information_query(self):
        return docs.User.objects(username=self.username)

    def course_list_query(self):
        try:
            information = self.information_query().next()
        except:
            return []
        course_information = information['course_info']
        course_list = []
        for course in course_information:
            course_name = course['caption']
            course_list.append(course_name)
        return course_list



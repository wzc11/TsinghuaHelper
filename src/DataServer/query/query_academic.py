__author__ = 'CaoYe'

from query import *


class query_academic(query):
    def timetable_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        result = information['timetable']
        return result

    def person_info_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        result = information['person_info']
        return result
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

    def term_list_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        result = []
        course_score_list = information['course_score']
        for term in course_score_list:
            result.append(term['school_term'])
        return result

    def score_info_query(self, course_sequence):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        course_score_list = information['course_score']
        result = course_score_list[course_sequence]
        return result


if __name__ == "__main__":
    import sys
    query_set = query_academic('oUfi4uCxAoWKGW52MoCW-b2THjCI')
    score_info = query_set.score_info_query(0)
    a = 1
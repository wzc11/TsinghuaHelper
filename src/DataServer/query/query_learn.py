__author__ = 'CaoYe'
# -*- coding: utf-8 -*-
from query import *
import datetime


class query_learn(query):
    def course_list_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        course_information = information['course_info']
        result_list = []
        for course in course_information:
            course_caption = course['caption']
            result_list.append(course_caption)
        return result_list

    def course_info_all_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        result = information['course_info']
        return result

    def course_info_query(self, course_sequence):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        course_information = information['course_info']
        result = course_information[course_sequence]
        return result

    def course_special_query(self, course_sequence):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        course_information = information['learn_info']
        result = course_information[course_sequence]
        return result

    def homework_info_query(self, course_sequence):
        special = self.course_special_query(course_sequence)
        result_list = special['homework']
        return result_list

    def notice_info_query(self, course_sequence):
        special = self.course_special_query(course_sequence)
        result_list = special['notice']
        return result_list

    def files_info_query(self, course_sequence):
        special = self.course_special_query(course_sequence)
        result_list = special['files']
        return result_list

    def days_get(self, date):
        d1 = datetime.datetime.today()
        d2 = datetime.datetime.strptime(date, '%Y-%m-%d')
        delta = d2 - d1
        return delta.days

    def homework_info_recent_query(self, course_sequence):
        special = self.course_special_query(course_sequence)
        result_list = []
        homework_list = special['homework']
        for homework in homework_list:
            if self.days_get(homework['date']) > -8:
                result_list.append(homework)
        return result_list

    def notice_info_recent_query(self, course_sequence):
        special = self.course_special_query(course_sequence)
        result_list = []
        notice_list = special['notice']
        for notice in notice_list:
            if self.days_get(notice['date']) > -8:
                result_list.append(notice)
        return result_list

    def files_info_recent_query(self, course_sequence):
        special = self.course_special_query(course_sequence)
        result_list = []
        files_list = special['files']
        for files in files_list:
            if self.days_get(files['date']) > -8:
                result_list.append(files)
        return result_list

    def course_attention_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        result = information['course_attention']
        return result

    def homework_uncommitted_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        course_information = information['learn_info']
        course_attention = self.course_attention_query()
        result_list = []
        for course in course_information:
            if not course['caption'] in course_attention:
                continue
            homework_course = {
                'caption': course['caption'],
                'homework': []
            }
            homework_list = course['homework']
            for homework in homework_list:
                if homework['state'] == '尚未提交'.decode('UTF-8'):
                    homework_course['homework'].append(homework)
            if len(homework_course['homework']) > 0:
                result_list.append(homework_course)
        return result_list

    def course_attention_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        result_list = information['course_attention']
        return result_list

    def my_table_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        course_information = information['learn_info']
        course_attention = self.course_attention_query()
        result = {}
        date_count = datetime.datetime.today() - datetime.timedelta(days=7)
        str_add = ''
        for i in range(15):
            if i == 14:
                str_add = '以后'.decode('UTF-8')
            else:
                str_add = ''
            result[i] = {
                'notice': [],
                'notice_num': 0,
                'notice_url': '#' + str(i) + 'b',
                'notice_id': str(i) + 'b',
                'homework': [],
                'homework_num': 0,
                'homework_url': '#' + str(i) + 'a',
                'homework_id': str(i) + 'a',
                'date': date_count.strftime('%Y-%m-%d') + str_add
            }
            date_count = date_count + datetime.timedelta(days=1)
        for course in course_information:
            course_caption = course['caption']
            if not course_caption in course_attention:
                continue
            for homework in course['homework']:
                if homework['state'] == '尚未提交'.decode('UTF-8'):
                    days_after = self.days_get(homework['deadline']) + 8
                    if days_after >= 7 and days_after <= 14:
                        result[days_after]['homework'].append({'caption': course_caption, 'data': homework._data})
                        result[days_after]['homework_num'] += 1
                    elif days_after >= 15:
                        result[14]['homework'].append({'caption': course_caption, 'data': homework._data})
                        result[14]['homework_num'] += 1
            for notice in course['notice']:
                days_after = self.days_get(notice['date']) + 8
                if days_after <= 7 and days_after >= 0:
                    result[days_after]['notice'].append({'caption': course_caption, 'data': notice._data})
                    result[days_after]['notice_num'] += 1
            result_list = []
            for i in range(15):
                result_list.append(result[i])
        return result_list


if __name__ == "__main__":
    import sys
    query_set = query_learn('oUfi4uNcdV3lvs_t7z1s7tiIsmvE')
    score_info = query_set.my_table_query()
    a = 1

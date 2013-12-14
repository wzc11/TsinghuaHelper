__author__ = 'CaoYe'
# -*- coding: utf-8 -*-
from query import *


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
                if homework['state'] == '尚未提交':
                    homework_course['homework'].append(homework)
            result_list.append(homework_course)
        return result_list

    def course_attention_query(self):
        try:
            information = self.all_information_query().next()
        except Exception, e:
            return []
        result_list = information['course_attention']
        return result_list
    # def course_info_query(self, course_caption):
    #     try:
    #         information = self.all_information_query().next()
    #     except:
    #         return []
    #     course_information = information['course_info']
    #     result_list = []
    #     for course in course_information:
    #         if course['caption'] == course_caption:
    #             result_list.append(course)
    #     return result_list
    #
    # def course_special_query(self, course_caption):
    #     try:
    #         information = self.all_information_query().next()
    #     except:
    #         return []
    #     course_information = information['learn_info']
    #     result_list = []
    #     for course in course_information:
    #         if course['caption'] == course_caption:
    #             result_list.append(course)
    #     return result_list
    #
    # def homework_list_query(self, course_caption):
    #     special_list = self.course_special_query(course_caption)
    #     result_list = []
    #     for special in special_list:
    #         homework_caption_list = []
    #         homework_list = special['homework']
    #         for homework in homework_list:
    #             homework_caption = homework['caption']
    #             homework_caption_list.append(homework_caption)
    #         result_list.append(homework_caption_list)
    #     return result_list
    #
    # def homework_info_query(self, course_caption, homework_caption):
    #     special_list = self.course_special_query(course_caption)
    #     result_list = []
    #     for special in special_list:
    #         homework_list = special['homework']
    #         for homework in homework_list:
    #             if homework['caption'] == homework_caption:
    #                 result_list.append(homework)
    #     return result_list
    #
    # def notice_list_query(self, course_caption):
    #     special_list = self.course_special_query(course_caption)
    #     result_list = []
    #     for special in special_list:
    #         notice_caption_list = []
    #         notice_list = special['notice']
    #         for notice in notice_list:
    #             notice_caption = notice['caption']
    #             notice_caption_list.append(notice_caption)
    #         result_list.append(notice_caption_list)
    #     return result_list
    #
    # def notice_info_query(self, course_caption, notice_caption):
    #     special_list = self.course_special_query(course_caption)
    #     result_list = []
    #     for special in special_list:
    #         notice_list = special['notice']
    #         for notice in notice_list:
    #             if notice['caption'] == notice_caption:
    #                 result_list.append(notice)
    #     return result_list
    #
    # def files_list_query(self, course_caption):
    #     special_list = self.course_special_query(course_caption)
    #     result_list = []
    #     for special in special_list:
    #         files_caption_list = []
    #         files_list = special['files']
    #         for files in files_list:
    #             files_caption = files['caption']
    #             files_caption_list.append(files_caption)
    #         result_list.append(files_caption_list)
    #     return result_list
    #
    # def files_info_query(self, course_caption, files_caption):
    #     special_list = self.course_special_query(course_caption)
    #     result_list = []
    #     for special in special_list:
    #         files_list = special['files']
    #         for files in files_list:
    #             if files['caption'] == files_caption:
    #                 print files
    #                 result_list.append(files)
    #     return result_list

# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

import docs
from hunter_learn import hunter_learn


class hunter_store(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def learn_store(self):
        learn = hunter_learn(self.username, self.password)
        info = learn.getInfo()
        course_info_list = []
        course_list = []
        for course in info:
            course_special = docs.Course(
                caption=course['caption'],
                id=course['id'],
                file_unread=course['file_unread'],
                homework=course['homework'],
                notice_unread=course['notice_unread']
            )
            course_list.append(course_special)

            course_info = learn.getSpecial(course['id'])

            notice_info = course_info['notice']
            notice_list = []
            for notice in notice_info:
                notice_special = docs.SpecialNotice(
                    link=notice['link'],
                    caption=notice['caption'],
                    teacher=notice['teacher'],
                    date=notice['date']
                )
                notice_list.append(notice_special)

            classinfo_info = course_info['classinfo']
            classinfo_list = []
            for classinfo in classinfo_info:
                classinfo_special = docs.SpecialClassinfo(
                    teacher_name=classinfo['teacher_name'],
                    teacher_email=classinfo['teacher_email']
                )
                #debuger.printer(classinfo)
                classinfo_list.append(classinfo_special)

            files_info = course_info['files']
            files_list = []
            for files in files_info:
                files_special = docs.SpecialFiles(
                    link=files['link'],
                    caption=files['caption'],
                    note=files['note'],
                    size=files['size'],
                    date=files['date']
                )
                files_list.append(files_special)

            homework_info = course_info['homework']
            homework_list = []
            for homework in homework_info:
                homework_special = docs.SpecialHomework(
                    cannot_submit=homework['cannot_submit'],
                    cannot_see_review=homework['cannot_see_review'],
                    caption=homework['caption'],
                    state=homework['state'],
                    link=homework['link'],
                    review_link=homework['review_link'],
                    date=homework['date'],
                    deadline=homework['deadline'],
                    size=homework['size']
                )
                homework_list.append(homework_special)

            resources_info = course_info['resources']
            resources_list = []
            for resources in resources_info:
                resources_special = docs.SpecialResources(
                    link=resources['link'],
                    caption=resources['caption'],
                    note=resources['note']
                )
                resources_list.append(resources_special)

            special_info = docs.Special(
                notice=notice_list,
                classinfo=classinfo_list,
                files=files_list,
                homework=homework_list,
                resources=resources_list
            )
            course_info_list.append(special_info)
        user = docs.User(
            username=self.username,
            student_number='',
            realname='',
            course_info=course_list,
            learn_info=course_info_list,
            homework_info=None,
            personal_info=None
        )
        user.save()


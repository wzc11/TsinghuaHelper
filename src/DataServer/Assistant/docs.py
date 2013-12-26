# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

from mongoengine import *
from mongoengine import context_managers
import pymongo

connect('learnDB', host='127.0.0.1', port=10001)


class SpecialNotice(EmbeddedDocument):
    link = StringField()
    caption = StringField()
    teacher = StringField()
    date = StringField()
    text = StringField()


class SpecialClassinfo(EmbeddedDocument):
    teacher_name = StringField()
    teacher_email = StringField()


class SpecialFiles(EmbeddedDocument):
    link = StringField()
    caption = StringField()
    note = StringField()
    size = StringField()
    date = StringField()


class SpecialHomework(EmbeddedDocument):
    caption = StringField()
    state = StringField()
    link = StringField()
    date = StringField()
    deadline = StringField()
    size = StringField()
    note = StringField()
    file = StringField()
    submit_file = StringField()


class SpecialResources(EmbeddedDocument):
    link = StringField()
    caption = StringField()
    note = StringField()


class Special(EmbeddedDocument):
    caption = StringField()
    notice = ListField(EmbeddedDocumentField(SpecialNotice))
    classinfo = ListField(EmbeddedDocumentField(SpecialClassinfo))
    files = ListField(EmbeddedDocumentField(SpecialFiles))
    homework = ListField(EmbeddedDocumentField(SpecialHomework))
    resources = ListField(EmbeddedDocumentField(SpecialResources))


class Course(EmbeddedDocument):
    caption = StringField()
    id = StringField()
    file_unread = StringField()
    homework = StringField()
    notice_unread = StringField()


class SingleCourse(EmbeddedDocument):
    revenue = StringField()
    teacher = StringField()
    caption = StringField()
    time = StringField()
    duration = StringField()
    type = StringField()
    day = StringField()


class PersonInfo(EmbeddedDocument):
    major = StringField()
    is_at_school = StringField()
    is_minor = StringField()
    is_second_degree = StringField()
    student_number = StringField()
    phone = StringField()
    identification = StringField()
    charge_type = StringField()
    is_register = StringField()
    nation = StringField()
    real_name = StringField()
    teach_class = StringField()
    department = StringField()
    birth_date = StringField()
    sex = StringField()
    email = StringField()
    graduate_date = StringField()


class CourseScoreInfo(EmbeddedDocument):
    course_caption = StringField()
    course_point = StringField()
    score = StringField()
    course_type = StringField()
    course_time = StringField()


class CourseScore(EmbeddedDocument):
    school_term = StringField()
    course_info = ListField(EmbeddedDocumentField(CourseScoreInfo))


class User(Document):
    user_name = StringField()
    user_id = StringField()
    use_password = StringField()
    fake_id = StringField()
    last_time = FloatField()
    score_final = FloatField()
    person_info = EmbeddedDocumentField(PersonInfo)
    course_attention = ListField(StringField())
    course_info = ListField(EmbeddedDocumentField(Course))
    learn_info = ListField(EmbeddedDocumentField(Special))
    timetable = ListField(EmbeddedDocumentField(SingleCourse))
    course_score = ListField(EmbeddedDocumentField(CourseScore))


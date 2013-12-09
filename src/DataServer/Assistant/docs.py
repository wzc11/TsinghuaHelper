# -*- coding: utf-8 -*-
__author__ = 'CaoYe'

from mongoengine import *
from mongoengine import context_managers
import pymongo

connect('learnDB')


class SpecialNotice(EmbeddedDocument):
    link = StringField()
    caption = StringField()
    teacher = StringField()
    date = StringField()


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


class AllHomework(EmbeddedDocument):
    subject = StringField()
    submitted_file_link = StringField()
    note = StringField()
    submitted_file_name = StringField()
    file_name = StringField()
    submitted_note = StringField()
    caption = StringField()
    file_link = StringField()


class Homework(EmbeddedDocument):
    homework = ListField(EmbeddedDocumentField(AllHomework))


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


class User(Document):
    user_name = StringField()
    user_id = StringField()
    use_password = StringField()
    course_info = ListField(EmbeddedDocumentField(Course))
    learn_info = ListField(EmbeddedDocumentField(Special))
    timetable = ListField(EmbeddedDocumentField(SingleCourse))
    homework_info = EmbeddedDocumentField(Homework)
    person_info = EmbeddedDocumentField(PersonInfo)


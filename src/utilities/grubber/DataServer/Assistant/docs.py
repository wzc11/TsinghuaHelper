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
    cannot_submit = StringField()
    cannot_see_review = StringField()
    caption = StringField()
    state = StringField()
    link = StringField()
    review_link = StringField()
    date = StringField()
    deadline = StringField()
    size = StringField()


class SpecialResources(EmbeddedDocument):
    link = StringField()
    caption = StringField()
    note = StringField()


class Special(EmbeddedDocument):
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


class Personal(EmbeddedDocument):
    email = StringField()
    name = StringField()
    gender = StringField()
    user_type = StringField()


class Course(EmbeddedDocument):
    caption = StringField()
    id = StringField()
    file_unread = StringField()
    homework = StringField()
    notice_unread = StringField()


class User(Document):
    username = StringField()
    student_number = StringField()
    realname = StringField()
    course_info = ListField(EmbeddedDocumentField(Course))
    learn_info = ListField(EmbeddedDocumentField(Special))
    homework_info = EmbeddedDocumentField(Homework)
    personal_info = EmbeddedDocumentField(Personal)


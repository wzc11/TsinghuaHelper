# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from store import store
from query import query
from pusher import pusher
from django.utils.encoding import smart_str
from urllib import *

import json
# Create your views here.

@csrf_exempt
def pushtest(request):
    t = pusher('oUO46t8JgZ8mrMc9d1bptXDJW04E')
    t.push('0')
    return HttpResponse(0)


@csrf_exempt
def cmd_handler(request):
    print(smart_str(request.body))
    result = {
        'error': -1,
        'data': []
    }
    try:
        object = json.loads(smart_str(request.body))
        cmd = object['type']
        if cmd == 'bind':
            result = bind(object['data'])
        elif cmd == 'course_list':
            result = course_list_get(object['data'])
        elif cmd == 'course_info':
            result = course_info_get(object['data'])
        elif cmd == 'homework_list':
            result = homework_list_get(object['data'])
        elif cmd == 'homework_info':
            result = homework_info_get(object['data'])
        elif cmd == 'notice_list':
            result = notice_list_get(object['data'])
        elif cmd == 'notice_info':
            result = notice_info_get(object['data'])
        elif cmd == 'files_list':
            result = files_list_get(object['data'])
        elif cmd == 'files_info':
            result = files_info_get(object['data'])
        return HttpResponse(json.dumps(result))
    except Exception, e:
        print Exception, e
        return HttpResponse(json.dumps(result))


def bind(object):
    result = {
        'error': 0,
        'data': []
    }
    store_set = store(object['username'], object['password'], object['user_id'])
    if not store_set.learn_store():
        result['error'] = 1
    return result


def course_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.course_list_query()
    result['data'] = course_lists
    return result


def course_info_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.course_info_query(object['course_caption'])
    if len(course_lists) == 0:
        result['error'] = 2
        return json.dumps(result)
    result['data'].append('课程名称:'.decode('UTF-8') + course_lists[0]._data['caption'])
    result['data'].append('课程编号:'.decode('UTF-8') + course_lists[0]._data['id'])
    result['data'].append('未读文件:'.decode('UTF-8') + course_lists[0]._data['file_unread'])
    result['data'].append('未交作业:'.decode('UTF-8') + course_lists[0]._data['homework'])
    result['data'].append('未读通知:'.decode('UTF-8') + course_lists[0]._data['notice_unread'])
    return result


def homework_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.homework_list_query(object['course_caption'])
    if len(course_lists) == 0:
        result['error'] = 2
        return result
    result['data'] = course_lists[0]
    return result


def homework_info_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.homework_info_query(object['course_caption'], object['homework_caption'])
    if len(course_lists) == 0:
        result['error'] = 2
        return result
    result['data'].append('作业标题:'.decode('UTF-8') + course_lists[0]._data['caption'])
    result['data'].append('能否提交:'.decode('UTF-8') + course_lists[0]._data['cannot_submit'])
    result['data'].append('是否批阅:'.decode('UTF-8') + course_lists[0]._data['cannot_see_review'])
    result['data'].append('作业状态:'.decode('UTF-8') + course_lists[0]._data['state'])
    result['data'].append('作业链接:'.decode('UTF-8') + course_lists[0]._data['link'])
    result['data'].append('批阅链接:'.decode('UTF-8') + course_lists[0]._data['review_link'])
    result['data'].append('作业日期:'.decode('UTF-8') + course_lists[0]._data['date'])
    result['data'].append('截止日期:'.decode('UTF-8') + course_lists[0]._data['deadline'])
    result['data'].append('文件大小:'.decode('UTF-8') + course_lists[0]._data['size'])
    return result


def notice_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.notice_list_query(object['course_caption'])
    if len(course_lists) == 0:
        result['error'] = 2
        return result
    result['data'] = course_lists[0]
    return result


def notice_info_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.notice_info_query(object['course_caption'], object['notice_caption'])
    if len(course_lists) == 0:
        result['error'] = 2
        return result
    result['data'].append('公告标题:'.decode('UTF-8') + course_lists[0]._data['caption'])
    result['data'].append('公告链接:'.decode('UTF-8') + [0]._data['link'])
    result['data'].append('公告教师:'.decode('UTF-8') + course_lists[0]._data['teacher'])
    result['data'].append('公告日期:'.decode('UTF-8') + course_lists[0]._data['date'])
    return result


def files_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.files_list_query(object['course_caption'])
    if len(course_lists) == 0:
        result['error'] = 2
        return result
    result['data'] = course_lists[0]
    return result


def files_info_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_lists = query_set.files_info_query(object['course_caption'], object['files_caption'])
    if len(course_lists) == 0:
        result['error'] = 2
        return result
    result['data'].append('文件标题:'.decode('UTF-8') + course_lists[0]._data['caption'])
    result['data'].append('文件链接:'.decode('UTF-8') + course_lists[0]._data['link'])
    result['data'].append('文件说明:'.decode('UTF-8') + course_lists[0]._data['note'])
    result['data'].append('文件大小:'.decode('UTF-8') + course_lists[0]._data['size'])
    result['data'].append('文件日期:'.decode('UTF-8') + course_lists[0]._data['date'])
    return result
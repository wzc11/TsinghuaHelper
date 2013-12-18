# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from store.store_learn import *
from store.store_academic import *
from query.query_learn import *
from query.query_wechat import *
from query.query_academic import *
from django.utils.encoding import smart_str
from django.shortcuts import render_to_response
from mythread.thread_grubber import *
from config import *
from urllib import *
import json
# Create your views here.


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
        if object['data']['user_id'] in user_lock_list:
            result['error'] = 3
            print json.dumps(result)
            return HttpResponse(json.dumps(result))
        #query = query_wechat(object['data']['user_id'])
        #fake_id = query.fake_id_query()
        if cmd == 'bind':
            result = bind(object['data'])
        elif cmd == 'fakeId':
            result = fake_id_store(object['data'])
        elif cmd == 'course_list':
            result = course_list_get(object['data'])
        elif cmd == 'homework_list':
            result = homework_list_get(object['data'])
        elif cmd == 'notice_list':
            result = notice_list_get(object['data'])
        elif cmd == 'files_list':
            result = files_list_get(object['data'])
        elif cmd == 'user_info':
            result = person_info_get(object['data'])
        elif cmd == 'focus':
            result = course_state_get_set(object['data'])
        elif cmd == 'deadline':
            result = deadline_list_get(object['data'])
        print json.dumps(result)
        return HttpResponse(json.dumps(result))
    except Exception, e:
        print Exception, e
        return HttpResponse(json.dumps(result))


def get_test():
    i = 0
    result = 0
    while i < 4:
        i = i + 1
        mid = random.randint(0, 9)
        result = result * 10 + mid
    return result


def bind(object):
    result = {
        'error': 0,
        'data': [],
        'test': get_test()
    }
    try:
        learn = hunter_learn(object['username'], object['password'])
        user_pass_list[object['user_id']] = [object['username'], object['password']]
    except userPassWrongException, e:
        result['error'] = 1
        return result
    except Exception, e:
        print Exception, e
        result['error'] = 2
    return result


def fake_id_store(object):
    result = {
        'error': 0,
        'data': []
    }
    user_lock_list.append(object['user_id'])
    try:
        user_info = user_pass_list[object['user_id']]
        object['username'] = user_info[0]
        object['password'] = user_info[1]
        del(user_pass_list[object['user_id']])
        grubber = thread_grubber(object)
        grubber.start()
    except Exception, e:
        print Exception, e
        result['error'] = 2
        user_lock_list.remove(object['user_id'])
    return result


def course_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query_learn(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_list = query_set.course_list_query()
    count = 0
    for course in course_list:
        course_url = '<a href="http://166.111.80.7:8081/courseInfo/' + object['user_id'] + '/' + str(count) + \
                     '/">' + course + '</a>'
        result['data'].append(course_url)
        count += 1
    return result


def homework_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query_learn(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_list = query_set.course_list_query()
    count = 0
    for course in course_list:
        course_url = '<a href="http://166.111.80.7:8081/homeworkInfo/' + object['user_id'] + '/' + str(count) + \
                     '/">' + course + '</a>'
        result['data'].append(course_url)
        count += 1
    return result


def notice_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query_learn(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_list = query_set.course_list_query()
    count = 0
    for course in course_list:
        course_url = '<a href="http://166.111.80.7:8081/noticeInfo/' + object['user_id'] + '/' + str(count) + \
                     '/">' + course + '</a>'
        result['data'].append(course_url)
        count += 1
    return result


def files_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query_learn(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_list = query_set.course_list_query()
    count = 0
    for course in course_list:
        course_url = '<a href="http://166.111.80.7:8081/filesInfo/' + object['user_id'] + '/' + str(count) + \
                     '/">' + course + '</a>'
        result['data'].append(course_url)
        count += 1
    return result


def person_info_get(object):
    result = {
        'error': 0,
        'url': 'http://166.111.80.7:8081/person_img/' + object['user_id'] + '/',
        'data': []
    }
    query_set = query_academic(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    person_info = query_set.person_info_query()
    result['data'].append('姓名:'.decode('UTF-8') + person_info['real_name'])
    result['data'].append('性别:'.decode('UTF-8') + person_info['sex'])
    result['data'].append('民族:'.decode('UTF-8') + person_info['nation'])
    result['data'].append('出生日期:'.decode('UTF-8') + person_info['birth_date'])
    result['data'].append('专业:'.decode('UTF-8') + person_info['major'])
    result['data'].append('学号:'.decode('UTF-8') + person_info['student_number'])
    result['data'].append('身份证号:'.decode('UTF-8') + person_info['identification'])
    result['data'].append('教学班:'.decode('UTF-8') + person_info['teach_class'])
    result['data'].append('院（系，所）:'.decode('UTF-8') + person_info['department'])
    result['data'].append('联系电话手机:'.decode('UTF-8') + person_info['phone'])
    result['data'].append('常用电子邮箱:'.decode('UTF-8') + person_info['email'])
    result['data'].append('是否在校:'.decode('UTF-8') + person_info['is_at_school'])
    result['data'].append('是否辅修:'.decode('UTF-8') + person_info['is_minor'])
    result['data'].append('第二学位否:'.decode('UTF-8') + person_info['is_second_degree'])
    result['data'].append('收费类别:'.decode('UTF-8') + person_info['charge_type'])
    result['data'].append('是否有学籍:'.decode('UTF-8') + person_info['is_register'])
    result['data'].append('毕业日期:'.decode('UTF-8') + person_info['graduate_date'])
    return result


def course_state_get_set(object):
    result = {
        'error': 0,
        'data': []
    }
    if object['update_flag'] == 'true':
        try:
            store_set = store_learn('', '', object['user_id'])
            store_set.course_attention_set(object['update_data'])
        except Exception, e:
            print Exception, e
            result['error'] = 2
    query_set = query_learn(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_list = query_set.course_list_query()
    course_attention_list = query_set.course_attention_query()
    for course in course_list:
        if course in course_attention_list:
            result['data'].append([course, True])
        else:
            result['data'].append([course, False])
    return result


def deadline_list_get(object):
    result = {
        'error': 0,
        'data': []
    }
    query_set = query_learn(object['user_id'])
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    result['data'] = 'http://166.111.80.7:8081/deadline_list/' + object['user_id'] + '/'
    return result


@csrf_exempt
def course_info_get(request, user_id, course_sequence):
    try:
        course_sequence = int(course_sequence)
    except ValueError:
        return HttpResponse(0)
    query_set = query_learn(user_id)
    course_info = query_set.course_info_query(course_sequence)
    content = course_info
    return render_to_response('template/course_info.html', {'content': content})


@csrf_exempt
def homework_info_get(request, user_id, course_sequence):
    try:
        course_sequence = int(course_sequence)
    except ValueError:
        return HttpResponse(0)
    query_set = query_learn(user_id)
    homework_info = query_set.homework_info_query(course_sequence)
    content = homework_info
    return render_to_response('template/homework_info.html', {'content': content})


@csrf_exempt
def notice_info_get(request, user_id, course_sequence):
    try:
        course_sequence = int(course_sequence)
    except ValueError:
        return HttpResponse(0)
    query_set = query_learn(user_id)
    notice_info = query_set.notice_info_query(course_sequence)
    content = notice_info
    return render_to_response('template/notice_info.html', {'content': content})


@csrf_exempt
def files_info_get(request, user_id, course_sequence):
    try:
        course_sequence = int(course_sequence)
    except ValueError:
        return HttpResponse(0)
    query_set = query_learn(user_id)
    files_info = query_set.files_info_query(course_sequence)
    content = files_info
    return render_to_response('template/files_info.html', {'content': content})


@csrf_exempt
def homework_uncommitted_info_get(request, user_id):
    query_set = query_learn(user_id)
    homework_uncommitted_info = query_set.homework_uncommitted_query()
    content = homework_uncommitted_info
    return render_to_response('template/homework_uncommitted_info.html', {'content': content})


# @csrf_exempt
# def person_info_get(request, user_id):
#     query_set = query_academic(user_id)
#     person_info = query_set.person_info_query()
#     content = person_info
#     return render_to_response('template/person_info.html', {'content': content})


@csrf_exempt
def person_img_get(request, user_id):
    image_data = open('C:\\Users\\ziyewuge\\Pictures\\TsinghuaHelper\\new\\' + user_id + '.jpg', "rb").read()
    return HttpResponse(image_data, mimetype="image/jpg")
    #return HttpResponse('C:\\Users\\Public\\Pictures\\TsinghuaHelper\\new\\' + user_id + '.jpg')

# def course_info_get(object):
#     result = {
#         'error': 0,
#         'data': []
#     }
#     query_set = query(object['user_id'])
#     if not query_set.user_id_exist():
#         result['error'] = 1
#         return result
#     course_lists = query_set.course_info_query(object['course_caption'])
#     if len(course_lists) == 0:
#         result['error'] = 2
#         return json.dumps(result)
#     result['data'].append('课程名称:'.decode('UTF-8') + course_lists[0]._data['caption'])
#     result['data'].append('课程编号:'.decode('UTF-8') + course_lists[0]._data['id'])
#     result['data'].append('未读文件:'.decode('UTF-8') + course_lists[0]._data['file_unread'])
#     result['data'].append('未交作业:'.decode('UTF-8') + course_lists[0]._data['homework'])
#     result['data'].append('未读通知:'.decode('UTF-8') + course_lists[0]._data['notice_unread'])
#     return result
#
#
# def homework_list_get(object):
#     result = {
#         'error': 0,
#         'data': []
#     }
#     query_set = query(object['user_id'])
#     if not query_set.user_id_exist():
#         result['error'] = 1
#         return result
#     course_lists = query_set.homework_list_query(object['course_caption'])
#     if len(course_lists) == 0:
#         result['error'] = 2
#         return result
#     result['data'] = course_lists[0]
#     return result
#
#
# def homework_info_get(object):
#     result = {
#         'error': 0,
#         'data': []
#     }
#     query_set = query(object['user_id'])
#     if not query_set.user_id_exist():
#         result['error'] = 1
#         return result
#     course_lists = query_set.homework_info_query(object['course_caption'], object['homework_caption'])
#     if len(course_lists) == 0:
#         result['error'] = 2
#         return result
#     result['data'].append('作业标题:'.decode('UTF-8') + course_lists[0]._data['caption'])
#     result['data'].append('能否提交:'.decode('UTF-8') + course_lists[0]._data['cannot_submit'])
#     result['data'].append('是否批阅:'.decode('UTF-8') + course_lists[0]._data['cannot_see_review'])
#     result['data'].append('作业状态:'.decode('UTF-8') + course_lists[0]._data['state'])
#     result['data'].append('作业链接:'.decode('UTF-8') + course_lists[0]._data['link'])
#     result['data'].append('批阅链接:'.decode('UTF-8') + course_lists[0]._data['review_link'])
#     result['data'].append('作业日期:'.decode('UTF-8') + course_lists[0]._data['date'])
#     result['data'].append('截止日期:'.decode('UTF-8') + course_lists[0]._data['deadline'])
#     result['data'].append('文件大小:'.decode('UTF-8') + course_lists[0]._data['size'])
#     return result
#
#
# def notice_list_get(object):
#     result = {
#         'error': 0,
#         'data': []
#     }
#     query_set = query(object['user_id'])
#     if not query_set.user_id_exist():
#         result['error'] = 1
#         return result
#     course_lists = query_set.notice_list_query(object['course_caption'])
#     if len(course_lists) == 0:
#         result['error'] = 2
#         return result
#     result['data'] = course_lists[0]
#     return result
#
#
# def notice_info_get(object):
#     result = {
#         'error': 0,
#         'data': []
#     }
#     query_set = query(object['user_id'])
#     if not query_set.user_id_exist():
#         result['error'] = 1
#         return result
#     course_lists = query_set.notice_info_query(object['course_caption'], object['notice_caption'])
#     if len(course_lists) == 0:
#         result['error'] = 2
#         return result
#     result['data'].append('公告标题:'.decode('UTF-8') + course_lists[0]._data['caption'])
#     result['data'].append('公告链接:'.decode('UTF-8') + [0]._data['link'])
#     result['data'].append('公告教师:'.decode('UTF-8') + course_lists[0]._data['teacher'])
#     result['data'].append('公告日期:'.decode('UTF-8') + course_lists[0]._data['date'])
#     return result
#
#
# def files_list_get(object):
#     result = {
#         'error': 0,
#         'data': []
#     }
#     query_set = query(object['user_id'])
#     if not query_set.user_id_exist():
#         result['error'] = 1
#         return result
#     course_lists = query_set.files_list_query(object['course_caption'])
#     if len(course_lists) == 0:
#         result['error'] = 2
#         return result
#     result['data'] = course_lists[0]
#     return result
#
#
# def files_info_get(object):
#     result = {
#         'error': 0,
#         'data': []
#     }
#     query_set = query(object['user_id'])
#     if not query_set.user_id_exist():
#         result['error'] = 1
#         return result
#     course_lists = query_set.files_info_query(object['course_caption'], object['files_caption'])
#     if len(course_lists) == 0:
#         result['error'] = 2
#         return result
#     result['data'].append('文件标题:'.decode('UTF-8') + course_lists[0]._data['caption'])
#     result['data'].append('文件链接:'.decode('UTF-8') + course_lists[0]._data['link'])
#     result['data'].append('文件说明:'.decode('UTF-8') + course_lists[0]._data['note'])
#     result['data'].append('文件大小:'.decode('UTF-8') + course_lists[0]._data['size'])
#     result['data'].append('文件日期:'.decode('UTF-8') + course_lists[0]._data['date'])
#     return result
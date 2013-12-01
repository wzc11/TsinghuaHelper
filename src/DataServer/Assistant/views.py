from django.shortcuts import render
from django.http import HttpResponse
from Assistant.hunter_query import hunter_query
# Create your views here.


def course_list_get(request):
    hunter = hunter_query('caoy11')
    course_list = hunter.course_list_query()
    result = ''
    for course in course_list:
        result = result + course
    return HttpResponse(result)

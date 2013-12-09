from django.conf.urls import patterns, include, url
from Assistant.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DataServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^person_img/([^/]+)/$', person_img_get),
    (r'^courseInfo/([^/]+)/(\d+)/$', course_info_get),
    (r'^homeworkInfo/([^/]+)/(\d+)/$', homework_info_get),
    (r'^noticeInfo/([^/]+)/(\d+)/$', notice_info_get),
    (r'^filesInfo/([^/]+)/(\d+)/$', files_info_get),
    url(r'^courseList/', cmd_handler),
)

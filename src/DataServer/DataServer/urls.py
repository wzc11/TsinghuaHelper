from django.conf.urls import patterns, include, url
from Assistant.views import *
from django.contrib import admin
from DataServer import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DataServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^person_img/([^/]+)/$', person_img_get),
    url(r'^person_old_img/([^/]+)/$', person_old_img_get),
    url(r'^deadline_list/([^/]+)/$', homework_uncommitted_info_get),
    url(r'^courseInfo/([^/]+)/(\d+)/$', course_info_get),
    url(r'^homeworkInfo/([^/]+)/(\d+)/$', homework_info_get),
    url(r'^noticeInfo/([^/]+)/(\d+)/$', notice_info_get),
    url(r'^filesInfo/([^/]+)/(\d+)/$', files_info_get),
    url(r'^courseList/', cmd_handler),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS[0],
         'show_indexes': True}),
)

from django.conf.urls import patterns, include, url
from Assistant.views import cmd_handler
from Assistant.views import pushtest
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DataServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', pushtest),
    url(r'^courseList/', cmd_handler),
)

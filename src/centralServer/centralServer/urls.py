from django.conf.urls import patterns, url
from wechatPlatform.views import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^weChat/$', weChatHandler),
    url(r'^weChat/login/$', weChatLogin),
    url(r'^weChat/focus/$', weChatFocus),
    url(r'^weChat/bind/$', weChatBind),
    #static resource url config
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS[0],
         'show_indexes': True}),
    # Examples:
    # url(r'^$', 'centralServer.views.home', name='home'),
    # url(r'^centralServer/', include('centralServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
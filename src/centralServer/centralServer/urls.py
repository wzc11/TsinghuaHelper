from django.conf.urls import patterns, url
from wechatPlatform.views import *
from wechatPlatform.viewsIndex import *
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
    url(r'^weChat/message/$', weChatMessage),
    url(r'^weChat/index/face/$', weChatFaceIndex),
    url(r'^weChat/index/learn/$', weChatLearnIndex),
    url(r'^weChat/index/facePK/$', weChatPKIndex),
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
# -*- coding: utf-8 -*-
__author__ = 'wangzhuqi.THU'

APP_ID = 'wx9ced5d9fffab8fee'
APP_SECRET = '3050fdbde346439d40fb0db2bd852bb5'
TOKEN = 'ziyewuge'
APP_TOKEN = {
    'access_token': '',
    'refresh_time': 0,
}

APP_INFO_CACHE = {'admin': {'usr': 'admin', 'pwd': 'admin'}}

APP_ACCOUNT = {
    'email': 'xz01234288@sina.com',
    'password': 'xz4288',
}

URL = {
    'ROOT': 'http://166.111.80.7/zywg_central/weChat/',
    'DATA': 'http://166.111.80.7/zywg_data/courseList/',
    'TEST': 'http://thusecretary.duapp.com/weChat/',
    'TOKEN': 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'
}

XML = {
    'TEXT_TEMPLATE': {
        'template': """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                </xml>""",

        'data-tag': ['to', 'from', 'time', 'content']
    },

    'USER_INFO_TEMPLATE': {
        'template': """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[news]]></MsgType>
                    <ArticleCount>1</ArticleCount>
                    <Articles>
                        <item>
                        <Title><![CDATA[%s]]></Title>
                        <Description><![CDATA[%s]]></Description>
                        <PicUrl><![CDATA[%s]]></PicUrl>
                        <Url><![CDATA[%s]]></Url>
                        </item>
                    </Articles>
                </xml>""",

        'data-tag': ['to', 'from', 'time', 'title', 'description', 'picUrl', 'link']
    },

    'INDEX_TEMPLATE': {
        'template': """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[news]]></MsgType>
                    <ArticleCount>1</ArticleCount>
                    <Articles>
                        <item>
                        <Title><![CDATA[%s]]></Title>
                        <Description><![CDATA[%s]]></Description>
                        <PicUrl><![CDATA[%s]]></PicUrl>
                        <Url><![CDATA[%s]]></Url>
                        </item>
                    </Articles>
                </xml>""",

        'data-tag': ['to', 'from', 'time', 'title', 'description', 'picUrl', 'link']
    },

    'IMAGE_TEXT_TEMPLATE': {
        'template': """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[news]]></MsgType>
                    <ArticleCount>%s</ArticleCount>
                    <Articles>
                        %s
                    </Articles>
                </xml>""",

        'data-tag': ['to', 'from', 'time', 'count', 'template-child']
    },

    'ITEM_TEXT_TEMPLATE': {
        'template': '''<item>
                    <Title><![CDATA[%s]]></Title>
                    <Description><![CDATA[%s]]></Description>
                    <PicUrl><![CDATA[%s]]></PicUrl>
                    <Url><![CDATA[%s]]></Url>
                    </item>''',

        'data-tag': ['title', 'description', 'url', 'link']
    }
}

APP_EVENT = {
    'score': '成绩\n',
    'course_list': '课程列表\n',
    'homework_list': '作业列表\n',
    'notice_list': '公告列表\n',
    'deadline': '未交作业\n',
    'files_list': '课程文件\n',
    'user_info': '个人信息\n',
    'unbind': '解除绑定\n'
}

APP_CARD = """
BEGIN:VCARD
FN:%s
ORG:%s
TEL:%s
EMAIL:%s
END:VCARD
"""

APP_VERSION = '4'
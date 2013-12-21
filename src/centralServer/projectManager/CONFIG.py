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
}

APP_EVENT = {
    'score': '成绩\n',
    'course_list': '课程列表\n',
    'homework_list': '作业列表\n',
    'notice_list': '公告列表\n',
    'deadline': '未交作业\n',
    'files_list': '课程文件\n',
    'user_info': '个人信息\n',
}

APP_HELP = '''使用帮助：\n
    系统设置：\n
        【一键绑定，网络学堂随身行】：点击系统设置菜单下的绑定账户，进入链接使用info账号密码即可完成绑定。\n
        【个人信息全获取】：绑定账户之后即可获取个人信息，学号头像各种信息一应俱全。\n
        【关注课程】：课程太多？选取部分课程进行关注省却无用信息。\n\n
    信息查询：\n
        成绩、课程、作业、公告？任何要求只需轻轻一点即可掌握。\n\n
    应用服务：\n
        【未交作业】：专注您所关注，提醒所有关注课程的未上交作业。\n
        【课程文件】：跟紧老师步伐，随时获取关注课程文件信息。\n
        【个人指数】：轻松一刻——屌丝、学霸、明星脸指数博您一笑。\n
        【个人名片】：极简主义,潇洒名片。'''
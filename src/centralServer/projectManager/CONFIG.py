__author__ = 'wangzhuqi.THU'

APP_ID = 'wx9ced5d9fffab8fee'
APP_SECRET = '3050fdbde346439d40fb0db2bd852bb5'
TOKEN = 'ziyewuge'
APP_TOKEN = {
    'access_token': '',
    'refresh_time': 0,
}

URL = {
    'DATA': 'http://59.66.138.37/courseList/',
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
                        <Url><![CDATA[Null]]></Url>
                        </item>
                    </Articles>
                </xml>""",

        'data-tag': ['to', 'from', 'time', 'title', 'description', 'picUrl']
    },
}
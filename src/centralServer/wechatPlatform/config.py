__author__ = 'wangzhuqi.THU'


config_token = 'ziyewuge'

config_xml = {
    'template': """<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[%s]]></MsgType>
             <Content><![CDATA[%s]]></Content>
             <FuncFlag>0</FuncFlag>
             </xml>""",

    'data-tag': ['to', 'from', 'time', 'type', 'content']
}


config_url = {
    'retrieval': 'http://59.66.138.37/courseList/',
    'test': 'http://thusecretary.duapp.com/weChat/',
}
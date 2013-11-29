__author__ = 'wangzhuqi.THU'
from django.utils.encoding import smart_str

import xml.etree.ElementTree as ET


class xmlHelper:
    def __init__(self, template):
        """


        :type self: list
        :param template: template format for the xml
        """
        self.template = template

    @staticmethod
    def parse(stringXML):
        """


        :type stringXML: str
        :param stringXML: the xml string we get
        :return: 'content': the list with all data or errors; 'err': 1 error, 0 data string
        """
        ret = {
            'err': 0,
            'content': {}
        }
        xml = ET.fromstring(stringXML)
        try:
            if xml.tag == 'xml':
                for child in xml:
                    ret['content'][child.tag] = smart_str(child.text)
            else:
                ret['err'] = 1
                ret['content']['err-info'] = 'do not receive a xml format string'
        except Exception, e:
            ret['err'] = 1
            ret['content']['err-info'] = smart_str(Exception) + ':' + smart_str(e)
            print 'xmlHelper.parse(dataXML)', Exception, ':', e

        return ret

    def generate(self, dataXML):
        """

        :type dataXML: list
        :param dataXML: data for xml template
        :return: 'content': the string converted from xml or error content; 'err': 1 error, 0 xml string
        """
        ret = {
            'err': 0,
            'content': ''
        }
        try:
            orderTag = []
            for elem in self.template['data-tag']:
                orderTag.append(dataXML[elem])
            ret['content'] = self.template['template'] % tuple(orderTag)
        except Exception, e:
            ret['err'] = 1
            ret['content'] = smart_str(Exception) + ':' + smart_str(e)
            print 'xmlHelper.generate(self, dataXML)', Exception, ':', e

        return ret
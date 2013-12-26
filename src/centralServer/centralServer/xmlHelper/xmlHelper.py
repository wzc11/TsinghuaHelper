__author__ = 'wangzhuqi.THU'
from django.utils.encoding import smart_str

import xml.etree.ElementTree as ET


class xmlHelper:
    @staticmethod
    def parse(stringXML):
        """
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

    @staticmethod
    def generate(dataXML, templateXML):
        """
        :param templateXML: template for generating xml file
        :param dataXML: data for xml template
        :return: 'content': the string converted from xml or error content; 'err': 1 error, 0 xml string
        """
        ret = {
            'err': 0,
            'content': ''
        }
        try:
            orderTag = []
            for elem in templateXML['data-tag']:
                appendStr = ''
                if elem == 'template-child':
                    template = dataXML[elem]['templateXML']
                    dataCollection = dataXML[elem]['collection']
                    print 'COLLECTION: ', dataCollection
                    for child_elem in dataCollection:
                        appendStr += xmlHelper.generate(child_elem, template)['content']
                else:
                    appendStr = dataXML[elem]
                orderTag.append(appendStr)
            ret['content'] = templateXML['template'] % tuple(orderTag)
        except Exception, e:
            ret['err'] = 1
            ret['content'] = smart_str(Exception) + ':' + smart_str(e)
            print 'xmlHelper.generate(self, dataXML)', Exception, ':', e

        #print ret
        return ret
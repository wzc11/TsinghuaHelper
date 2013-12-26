__author__ = 'wangzhuqi.THU'
from baseReqHelper import baseReqHelper


class reqHelper(baseReqHelper):
    def sentTextMsg(self, sendTo, content):
        """
        send a text message to user, the interval between two sending events
        should be more than 2s
        :type self: object
        :param sendTo: target user
        :param content: message content
        :return: True or False
        """
        msg = self._sendMsg(sendTo, {
            'type': 1,
            'content': content
        })
        return msg == 'ok'

    def Authorize(self, code):
        return self._getFakeId(code)
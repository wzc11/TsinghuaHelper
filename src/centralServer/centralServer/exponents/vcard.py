# -*- coding: utf-8 -*-
import qrcode
import os
from PIL import Image
from projectManager.CONFIG import *
'''vstr = """
BEGIN:VCARD
FN:曹晔
ORG:software
TEL:18810305395
EMAIL:wzc11@mails.tsinghua.edu.cn
END:VCARD
"""
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,   
    box_size=2,  
    border=20,  
)  
qr.add_data(vstr)  
qr.make(fit=True)  
img = qr.make_image()
img_central = img.resize((300, 300))
img_back = Image.new("RGB", (540, 300), 'white')
img_back.paste(img_central, (120, 0, 420, 300))
savePath = os.path.dirname(__file__).replace('\\', '/') + "/../static/img/card/" + "wzq" + '.jpg'
print os.path.isfile(savePath)
#img_back.save(savePath)
img.save(savePath)'''


def generateCard(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=5,
    )
    qr2 = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=0,
    )
    vstr = APP_CARD % tuple([data['name'], data['major'], data['phone'], data['email']])
    qr.add_data(vstr)
    qr2.add_data(vstr)
    qr.make(fit=True)
    qr2.make(fit=True)
    img = qr.make_image()
    img2 = qr2.make_image()
    img_central = img.resize((300, 300))
    img_back = Image.new("RGB", (540, 300), 'white')
    img_back.paste(img_central, (120, 0, 420, 300))
    savePath = os.path.dirname(__file__).replace('\\', '/') + "/../static/img/card/" \
               +data['openId'] + APP_VERSION + '.jpg'
    savePath2 = os.path.dirname(__file__).replace('\\', '/') + "/../static/img/card/" \
               +data['openId'] + APP_VERSION + '_2.jpg'
    img_back.save(savePath)
    img2.save(savePath2)
    return


def retrieveCard(data):
    path = os.path.dirname(__file__).replace('\\', '/') + "/../static/img/card/" \
           +data['openId'] + APP_VERSION + '.jpg'
    url = URL['ROOT'] + '../static/img/card/' \
          +data['openId'] + APP_VERSION + '.jpg'
    url2 = URL['ROOT'] + 'card/?src=/zywg_central/static/img/card/' \
          +data['openId'] + APP_VERSION + '_2.jpg'
    if os.path.isfile(path):
        return [url, url2]
    else:
        generateCard(data)
        return [url, url2]


def deleteCard(data):
    path = os.path.dirname(__file__).replace('\\', '/') + "/../static/img/card/" \
           + data['openId'] + APP_VERSION + '.jpg'
    path2 = os.path.dirname(__file__).replace('\\', '/') + "/../static/img/card/" \
           + data['openId'] + APP_VERSION + '_2.jpg'
    if os.path.isfile(path):
        os.remove(path)
    if os.path.isfile(path2):
        os.remove(path2)

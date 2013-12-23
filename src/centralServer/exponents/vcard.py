import qrcode
vstr = """ 
BEGIN:VCARD 
FN:wangzhicheng 
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
img=qr.make_image()  
img.save('wzc.jpg')
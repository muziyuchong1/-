# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import qrcode
import io

def get_code_by_str(text):
    if isinstance(text,str):
        print('请输入一组字符串')
        return None
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img_data = io.BytesIO()
    img.save(img_data)
    return img_data


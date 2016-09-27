# -*-coding:utf-8-*-

import qrcode
import requests
from PIL import Image


class QrCode:
    def __init__(self, version=8,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=4,
                 border=1,
                 save_path_name="二维码",
                 cont='您的二维码信息没有生成，请重试',
                 path='',
                 logo=''
                 ):

        self.version = version  # 值范围为1~40,控制二维码的大小， None 并使用 fit 参数即可

        self.error_correction = error_correction  # 纠错能力 _L约7%,_M约15%,_H约30%

        self.box_size = box_size  # 控制二维码中每个小个子包含的像素数

        self.border = border  # 边框值，最小为4

        self.name = save_path_name

        self.cont = cont

        self.save_path_name = save_path_name

        self.logo = logo

    def save(self):

        qr = qrcode.QRCode(

            version=self.version,

            error_correction=self.error_correction,

            box_size=self.box_size,

            border=self.border,

        )

        qr.add_data(self.cont)

        qr.make(fit=True)

        img = qr.make_image()

        img = img.convert('RGBA')

        icon = Image.open(self.logo)

        img_w, img_h = img.size

        factor = 0.25

        size_w, size_h = (int(img_w * factor), int(img_h * factor))

        print factor

        icon = icon.resize((size_w, size_h), Image.ANTIALIAS)

        w, h = (int(img_w * (1 - factor) / 2), int(img_h * (1 - factor) / 2))

        icon = icon.convert('RGBA')

        img.paste(icon, (w, h), icon)

        img.save(self.save_path_name)

        img.show()


for line in open('salers'):
    datas = line.strip('\n').split(',')
    salerid = datas[0]
    url = datas[1]

    conn = requests.get(url)

    name = salerid + '.png'
    f = open(name, 'wb')
    f.write(conn.content)
    f.close()

    saler_bd_url = "http://www.jb51.net/article/58579.htm"
    dest = 'leaderqr' + salerid + '.png'
    img = QrCode(cont=saler_bd_url, save_path_name=dest, logo=name)

    img.save()


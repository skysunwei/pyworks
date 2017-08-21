# coding:utf-8

import os
import sys
import csv
import string
import quopri
import datetime

type = sys.getfilesystemencoding()

vcf = 'BEGIN:VCARD\nVERSION:2.1\nN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;%s;;;\n' \
    'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:%s\n' \
    'TEL;CELL:%s\nEND:VCARD\n'

file = csv.reader(file('saler.csv', 'rb'))

guwens = {}
zxss = {}

delset = string.punctuation

for line in file:

    zxs = line[1]
    guwen = line[2]

    if guwens.has_key(guwen) is False:
        guwens[guwen] = {}
    guwens[guwen][zxs] = []

    if zxss.has_key(zxs) is False:
        zxss[zxs] = []

    contact = '%s:%s(%s%s%s)' % (line[8], line[4], line[5], line[6], line[7])
    zxss[zxs].append(contact)


date_folder = datetime.datetime.now().strftime('%Y-%m-%d')

if os.path.exists(date_folder) is False:
    os.makedirs(date_folder)

for guwen in guwens:
    folder_guwen = date_folder + '/' + guwen.translate(None, delset)

    if os.path.exists(folder_guwen) is False:
        os.makedirs(folder_guwen)

    for zxs in guwens[guwen]:

        f = open(folder_guwen + '/' + zxs.translate(None, delset) + '.vcf', "w+")

        for contact in zxss[zxs]:
            info = contact.split(':')
            tel = info[0]
            shopping = info[1].decode(type).encode('utf-8')
            detail = quopri.encodestring(shopping)

            f.writelines(vcf % (detail, detail, tel))

        f.close()

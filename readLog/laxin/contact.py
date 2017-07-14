# coding:utf-8

import os
import quopri
import csv
import datetime

vcf = 'BEGIN:VCARD\nVERSION:2.1\nN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;%s;;;\n' \
    'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:%s\n' \
    'TEL;CELL:%s\nEND:VCARD\n'

file = csv.reader(file('saler.csv', 'rb'))

guwens = {}
zxss = {}

for line in file:

    zxs = line[1]
    guwen = line[2]

    if guwens.has_key(guwen) is False:
        guwens[guwen] = {}
    guwens[guwen][zxs] = []

    if zxss.has_key(zxs) is False:
        zxss[zxs] = []

    contact = '%s:%s(%s在%s购买%s)' % (line[8], line[4], line[5], line[6].strip('2017-'), line[7])
    zxss[zxs].append(contact)


date_folder = datetime.datetime.now().strftime('%Y-%m-%d')
os.makedirs(date_folder)

for guwen in guwens:
    folder_guwen = date_folder + '/' + guwen
    os.makedirs(folder_guwen)

    for zxs in guwens[guwen]:

        f = open(folder_guwen + '/' + zxs + '.vcf', "w+")

        for contact in zxss[zxs]:
            info = contact.split(':')
            tel = info[0]
            detail = quopri.encodestring(info[1])

            f.writelines(vcf % (detail, detail, tel))

        f.close()

print 'done'
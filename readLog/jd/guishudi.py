#-*- coding: UTF-8 -*-

import sys
import requests
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf-8')

#---------

phones = []

for line in open('data'):
    datas = line.strip('\n').split('\t')
    phones.append(datas[1])

phones = list(set(phones))

print len(phones)

#---------

i = 1
provs = []
outs = []

url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel='

for phone in phones:

    try:
        page = requests.get(url + phone)

        if page.status_code == 200:

            try:
                prov = str(page.text).split(',')[1].split(':')[1]

                print i, ':', phone, prov

                provs.append(prov)
                outs.append(phone + ',' + prov.strip('\'') + '\n')
            except:
                continue
        else:
            print page.status_code

        i += 1
    except:
        continue

print(Counter(provs))

#---------

f = file('all.csv', "w+")

for line in outs:
    f.writelines(line)

f.close()

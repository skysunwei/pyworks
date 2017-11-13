#-*- coding: UTF-8 -*-

import itertools

file_name = 'data.txt'

Coupon = 158
FanWei = 10
N_Pin_Zu = 4
Filter_Words = ['蛋糕', '大闸蟹']


class Merchtype(object):
    merchandiseId = 0
    merchandiseName = ''
    merchandiseTag = ''

    name = ''
    money = 0.00

    def __init__(self, merchandiseId, merchandiseName, merchandiseTag, name, price, qimai):
        self.merchandiseId = merchandiseId
        self.merchandiseName = merchandiseName
        self.merchandiseTag = merchandiseTag
        self.name = name

        if qimai is 0:
            self.money = price
        else:
            self.money = price * qimai
    pass

price_group = {}

for line in open(file_name):
    datas = line.strip('\n').split(',')

    try:
        merchandiseId = int(datas[0])
        merchandiseName = datas[1]
        merchandiseTag = datas[2]

        name = datas[3]
        price = float(datas[4])

        qimai = int(datas[5])
    except:
        print line

    if (merchandiseTag == '不可用券') is True:
        continue

    has_word = False

    for word in Filter_Words:
        if word in merchandiseName:
            has_word = True
            break

        # print merchandiseName
    if has_word is True:
        continue

    merchtype = Merchtype(merchandiseId, merchandiseName, merchandiseTag, name, price, qimai)

    price_key = round(price * qimai, 2) if qimai != 0 else price

    if price in price_group.keys():
        price_group[price_key].append(merchtype)
    else:
        price_group[price_key] = [merchtype]


prices = price_group.keys()
price_all_zuhe = []

for i in range(1, N_Pin_Zu):
    iter = itertools.combinations(prices, i)
    price_all_zuhe.append(list(iter))

output_data = []

for items in price_all_zuhe:
    for item in items:
        zongjia = sum(item)

        gape = zongjia - Coupon

        if (gape < FanWei) and (gape > 0):
            output_data.append(item)
            # print item, zongjia

output = open('result.csv', 'w')

for items in output_data:
    for item in items:

        for merchtype in price_group[item]:
            output.writelines('%s(%s: %s),' % (merchtype.merchandiseName, merchtype.name, merchtype.money))
        output.writelines('\n')

    output.writelines('%s,\n\n' % sum(items))

output.close()

print 'done'
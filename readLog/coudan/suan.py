#-*- coding: UTF-8 -*-


file_name = 'data.txt'

Coupon = 148
FanWei = 10


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

all_merchtypes = []


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

    all_merchtypes.append(Merchtype(merchandiseId, merchandiseName, merchandiseTag, name, price, qimai))


output = open('result.csv', 'w')

for i in range(len(all_merchtypes)):
    money = all_merchtypes[i].money

    for j in range(i+1, len(all_merchtypes)):

        shiji = money + all_merchtypes[j].money - Coupon

        if (shiji < FanWei) and (shiji > 0):

            output.writelines('%s(%s - %s)[%s]' % (all_merchtypes[i].merchandiseName, all_merchtypes[i].name, all_merchtypes[i].money, all_merchtypes[i].merchandiseTag))
            output.writelines(',')
            output.writelines('%s(%s - %s)[%s]' % (all_merchtypes[j].merchandiseName, all_merchtypes[j].name, all_merchtypes[j].money, all_merchtypes[j].merchandiseTag))
            output.writelines(',')
            output.writelines(str(money + all_merchtypes[j].money))

            output.writelines('\n')

output.close()

print 'done'
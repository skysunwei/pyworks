# coding:utf-8

import json


def send_coupon():

    print '渠道,金额,张数,优惠券编号'

    for line in open('test'):
        datas = line.strip('\n').split(',')

        vars = datas[1].split('a:5:')[1].split(';')

        print datas[0], ',', \
            int(vars[9].split(':')[2])/100, ',', \
            vars[3].split(':')[1], ',', \
            vars[5].split(':')[1]


def saler_upgrade():
    for line in open('upgrade'):

        datas = line.strip('\n').split(',')

        print datas[1], datas[4], datas[2].split(';')[1].split(':')[2], datas[3].split(';')[1].split(':')[1]




saler_upgrade()


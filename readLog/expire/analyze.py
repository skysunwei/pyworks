import csv
# coding:utf-8

import time, datetime

file = csv.reader(file('warehouse.csv', 'rb'))

lines = []
for line in file:
    lines.append(line)

merchandise = {}

key = 0.3

for line in lines:
    # print line

    merchandiseId = int(line[0])
    merchandiseName = line[1]
    merchandiseQuantiy = int(line[2])

    expireDays = int(line[3])

    sourceNo = line[4]
    num = int(line[5])

    t = time.strptime(line[6], "%Y-%m-%d")
    y, m, d = t[0:3]
    days_interval = (datetime.datetime.now() - datetime.datetime(y, m, d)).days

    if days_interval >= expireDays*(1 - key):

        qit = []

        for readline in lines:
            if int(readline[0]) == merchandiseId and line[6] < readline[6]:
                # print qit
                qit.append(int(readline[5]))

        # print len(qit)

        if len(qit) == 0:
            print days_interval, expireDays * (1 - key)
            print 'now:', merchandiseId, merchandiseName, sourceNo,merchandiseQuantiy
        elif sum(qit) < merchandiseQuantiy:
            print days_interval, expireDays * (1 - key)
            print 'history:', merchandiseId, merchandiseName, sourceNo, merchandiseQuantiy, sum(qit)

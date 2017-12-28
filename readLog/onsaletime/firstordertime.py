#-*- coding: UTF-8 -*-

import csv
import time
import datetime

csvfile = file('merchandise.csv', 'rb')

output = {}
dateinfo = {}

for line in csv.reader(csvfile):
    # print line[1]

    if output.has_key(line[2]) is False:
        output[line[2]] = '%s(%s) | %s(%s), ' % (line[1], line[0], line[3], line[2])

    if dateinfo.has_key(line[2]):
        dateinfo[line[2]].append(line[4])
    else:
        dateinfo[line[2]] = [line[4]]

    # break

# print output

for merchid in dateinfo.keys():

    dates = dateinfo[merchid]
    dates.sort(reverse=True)

    # print dates
    # print len(dates)

    lenth = len(dates)

    for i in range(0, lenth - 1):

        if i == lenth - 2:
            print output[merchid], dates[i]
            break

        try:
            ti = time.strptime(dates[i], "%Y-%m-%d")
            ti1 = time.strptime(dates[i+1], "%Y-%m-%d")
            yi, mi, di = ti[0:3]
            yi1, mi1, di1 = ti1[0:3]

            if (datetime.datetime(yi, mi, di) - datetime.datetime(yi1, mi1, di1)).days >= 30:
                print output[merchid], dates[i]
                break
        except Exception, e:
            print Exception, ":", e
            exit()


    # break


# print dateinfo

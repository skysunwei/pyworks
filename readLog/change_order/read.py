# coding: utf-8

import csv

# csvfile = file('rank_2016-07-29.csv', 'rb')
# reader = csv.reader(csvfile)

for line in open('new'):
    datas = line.strip('\n').split(',')
    print 'insert `op-sunwei-merchtype-mapping`(`merchtypeid`,`product`) values(' + \
          str(datas[0]) + ', \'' + datas[1] + '\');'

# csvfile.close()
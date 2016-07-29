# coding: utf-8

import csv

csvfile = file('rank_2016-07-29.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print 'insert `op-sunwei-merchtype-mapping`(`merchtypeid`,`product`) values(' + \
          str(line[0]) + ', \'' + line[3] + '\');'

csvfile.close() 
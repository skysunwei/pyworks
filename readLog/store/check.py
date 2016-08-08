#-*- coding: UTF-8 -*-

import csv
import datetime


expire_days = {}
backup_goods = {}

for line in open('strategy'):
    values = line.strip('\n').split(',')
    expire_days[values[0]] = values[2]
    backup_goods[values[0]] = values[3]

# print expire_days
# print backup_goods

current_time = datetime.datetime.now()
print '时间 :', current_time

reader = csv.reader(file('20160805171905.csv', 'rb'))

fist_line = True

for line in reader:

    if fist_line is True:
        fist_line += False
        continue

    product_id = line[0]
    product_name = line[1]
    # print product_id

    # time
    import_time_str = line[2]
    import_time = datetime.datetime.strptime(import_time_str, "%Y%m%d")
    time_interval = current_time - import_time
    # print time_interval.days

    if product_id in expire_days.keys():
        if time_interval.days > expire_days[product_id]:
            print product_name, ', 将要过期!'
    else:
        print product_name, '新增库存,请添加'

    # goods

    current_goods = line[3]
    # print current_goods

    if product_id in backup_goods.keys():
        if int(current_goods) < backup_goods[product_id]:
            print product_name, ', 需要补货!'
    else:
        print product_name, '新增库存,请添加'

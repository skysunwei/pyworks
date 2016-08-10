#-*- coding: UTF-8 -*-

import csv
import time
import datetime


expire_days = {}
backup_goods = {}


def read_strategy():
    for line in open('strategy'):
        values = line.strip('\n').split(',')
        expire_days[values[0]] = values[2]
        backup_goods[values[0]] = values[3]

# print expire_days
# print backup_goods

current_time = datetime.datetime.now()
# print '时间 :', current_time

source_file_name = '20160810110315.csv'


def make_sql(file_name):

    print 'truncate table `op-sunwei-store`;'

    reader = csv.reader(file(file_name, 'rb'))

    fist_line = True

    for line in reader:

        if fist_line is True:
            fist_line += False
            continue

        product_code = line[0]
        product_name = line[1].decode('utf8')[4:].encode('utf8')

        # time
        import_time_read = line[2]
        try:
            import_time = time.strptime(import_time_read, "%Y%m%d")
        except:
            try:
                import_time = time.strptime(import_time_read, "%Y-%m-%d")
            except:
                print 'time format error!'

        import_time_str = time.strftime("%Y-%m-%d", import_time)
        import_num = line[3]
        real_num = line[4]
        danwei = line[5]

        print 'insert `op-sunwei-store`(`code`,`name`,`time`,`num`,`real`, `danwei`) ' \
              'values(\'%s\',\'%s\',\'%s\',%s,%s,\'%s\');'% \
              (product_code, product_name, import_time_str, import_num, real_num, danwei)


def verify(file_name):
    read_strategy()

    reader = csv.reader(file(file_name, 'rb'))

    fist_line = True

    for line in reader:

        if fist_line is True:
            fist_line += False
            continue

        product_id = line[0]
        product_name = line[1].decode('utf8')[4:].encode('utf8')
        # print product_id

        # time
        import_time_str = line[2]
        try:
            import_time = datetime.datetime.strptime(import_time_str, "%Y%m%d")
        except:
            try:
                import_time = datetime.datetime.strptime(import_time_str, "%Y-%m-%d")
            except:
                print 'time format error!'

        time_interval = current_time - import_time
        # print time_interval.days

        if product_id in expire_days.keys():
            if time_interval.days >= expire_days[product_id]:
                print product_name, ', 将要过期!'
            # else:
            #     print product_id, product_name, '新增库存,请添加'

        # goods

        current_goods = line[3]
        # print current_goods

        if product_id in backup_goods.keys():
            print current_goods, backup_goods[product_id]
            if int(current_goods) <= int(backup_goods[product_id]):
                print product_name, ', 需要补货!'
            else:
                print product_name, '报警库存:', backup_goods[product_id], '当前库存:', current_goods, '不用补货'


make_sql(source_file_name)

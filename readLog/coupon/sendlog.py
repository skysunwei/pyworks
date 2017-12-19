# coding: utf-8

import csv


def read_log(log):
    result = {}

    if log.find('a:', 0) == 0:
        details = log.split(':', 2)
        detail_datas = details[2].strip('{').strip('}').split(';')

        for i in range(0, int(details[1])):
            try:
                result[read_log(detail_datas[i * 2])] = read_log(detail_datas[i * 2 + 1])
            except Exception, e:
                print detail_datas[i * 2]
                print e
                exit()

        return result

    if log.find('i:', 0) == 0:
        return int(log.split(':')[1])

    if log.find('s:', 0) == 0:
        return log.split(':')[2].strip('"')


def send_coupon():

    output_file_name = 'sendcoupons.csv'

    output_file = file(output_file_name, 'wb')
    writer = csv.writer(output_file)

    headline = []
    headline.append('发放时间')
    headline.append('渠道')
    headline.append('金额')
    headline.append('数量')
    headline.append('团长ID')
    headline.append('团长人数')
    headline.append('优惠券编号')

    writer.writerow(headline)

    for line in open('sendlog'):
        datas = line.strip('\n').split('\t')

        if datas[0] == 'time':
            continue

        try:
            temp = read_log(datas[2])

            dateline = str(datas[0]), \
                       datas[1], \
                       temp['money'], \
                       temp['num'], \
                       temp['salerid'], \
                       len(temp['salerid'].strip('"').split(',')), \
                       temp['couponid']

            writer.writerow(dateline)

        except Exception, e:
            print read_log(datas[2])
            print Exception, ":", e
            exit()

    output_file.close()

    print 'done'

send_coupon()
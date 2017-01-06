# coding: utf-8

import csv

def send_coupon():

    output_file_name = 'sendcoupons.csv'

    output_file = file(output_file_name, 'wb')
    writer = csv.writer(output_file)

    headline = []
    headline.append('发放时间')
    headline.append('渠道')
    headline.append('金额')
    headline.append('数量')
    headline.append('优惠券编号')

    writer.writerow(headline)

    for line in open('sendlog'):
        datas = line.strip('\n').split('\t')

        if datas[0] == 'time':
            continue

        try:
            vars = datas[2].split('a:5:')[1].split(';')

            dateline = str(datas[0]), datas[1], int(vars[9].split(':')[2].strip('"'))/100, vars[3].split(':')[1], vars[5].split(':')[1]

            writer.writerow(dateline)
        except:
            print line
            exit()

    output_file.close()

    print 'done'

send_coupon()
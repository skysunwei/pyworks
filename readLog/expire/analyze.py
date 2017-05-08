# coding:utf-8

import csv
import time, datetime

csv_file = csv.reader(file('warehouse.csv', 'rb'))

lines = []
for data in csv_file:
    lines.append(data)

merchandise = {}

key = 0.33

header = 'SKU编号,货物名称,入库单号,入库时间,库内保存天数,已经入库天数,2/3预警天数,过期SKU数量,当前库存数量'

output_file_name = time.strftime('%Y-%m-%d',time.localtime(time.time())) + '.csv'
output_file = file(output_file_name, 'wb')
writer = csv.writer(output_file)

writer.writerow(header.split(','))

output_lines = []

for line in lines:

    merchandiseId = int(line[0])
    merchandiseName = line[1]
    merchandiseQuantiy = int(line[2])

    expireDays = int(line[3])

    sourceNo = line[4]
    num = int(line[5])

    updateTime = line[6]

    t = time.strptime(updateTime, "%Y-%m-%d %H:%M:%S")
    y, m, d = t[0:3]
    days_interval = (datetime.datetime.now() - datetime.datetime(y, m, d)).days - 1  # 当天不算

    if days_interval >= expireDays * (1 - key):

        output_line = []
        # print line
        # print merchandiseName
        # print days_interval

        qit = []

        for read_line in lines:
            if int(read_line[0]) == merchandiseId and updateTime < read_line[6]:
                # print read_line
                qit.append(int(read_line[5]))

        # print len(qit), qit

        if len(qit) == 0:
            output_line.append(merchandiseId)
            output_line.append(merchandiseName)
            output_line.append(sourceNo)
            output_line.append(updateTime)
            output_line.append(expireDays)
            output_line.append(days_interval)
            output_line.append(round(expireDays* (1 - key), 2))
            output_line.append(merchandiseQuantiy)
            output_line.append(merchandiseQuantiy)

            output_lines.append(output_line)
        elif sum(qit) < merchandiseQuantiy:
            output_line.append(merchandiseId)
            output_line.append(merchandiseName)
            output_line.append(sourceNo)
            output_line.append(updateTime)
            output_line.append(expireDays)
            output_line.append(days_interval)
            output_line.append(round(expireDays * (1 - key), 2))
            output_line.append(merchandiseQuantiy - sum(qit))
            output_line.append(merchandiseQuantiy)

            output_lines.append(output_line)

# print output_lines

writer.writerows(output_lines)

output_file.close()

print 'done'
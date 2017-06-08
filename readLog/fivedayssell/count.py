import os
import csv
import time, datetime


def day_str_to_datetime(day_str):
    t = time.strptime(day_str, "%Y-%m-%d")
    return datetime.datetime(*t[:3])


def define_five(example):
    out = ''
    for i in range(0, len(example)-1):
        if example[i+1] - example[i] is not 1:
            out += ','
        else:
            out += '1'
    return out


def lianxu_order_day(datas, day_num):
    user_ids = []

    for line in datas:

        user_id = int(line[0])
        #
        # if user_id != 237:
        #     continue

        days = line[1].split(',')
        days.sort()

        # print days

        first_day = day_str_to_datetime(days[0])

        # print first_day

        day_intervals = [0]

        for day in days[1:]:
            current_day = day_str_to_datetime(day)
            day_intervals.append((current_day - first_day).days)

        # print len(day_intervals)

        one_day_intervals = define_five(day_intervals)

        # print one_day_intervals

        for one_days in one_day_intervals.split(','):
            if len(one_days) >= day_num:
                user_ids.append(str(user_id) + '\n')
                break

    return user_ids

all_data = []

csv_file = csv.reader(file('saler_17_5.csv', 'rb'))

for data in csv_file:
    all_data.append(data)

print len(all_data)

month = 5
folder = '%syue-%sren/' % (str(month), len(all_data))
os.makedirs(folder)

levels = [5, 10, 20, 30]


for level in levels:
    result = lianxu_order_day(all_data, level - 1)
    filename = 'lianxu%sdan-%sren.txt' % (level, len(result))
    print len(result)

    f = file(folder + filename, "w+")
    f.writelines(result)
    f.close()
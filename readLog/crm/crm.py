# coding:utf-8


import csv
import time, datetime

now_active = {}
now_not_active = {}

all = []
new = []
now_good_active = []
now_good_not_active = []
now_bad_active = []
now_bad_not_active = []
lost = []


file = csv.reader(file('user.csv', 'rb'))


def get_days_interval(order_day):
    try:
        t = time.strptime(order_day, "%Y-%m-%d")
        y, m, d = t[0:3]
        return (datetime.datetime.now() - datetime.datetime(y, m, d)).days
    except:
        return 10000


def median(my_list):

    data = sorted(my_list)
    size = len(data)

    if size % 2 == 0:
        return (data[size//2]+data[size//2-1])/2

    return data[(size-1)//2]


for line in file:

    # print line

    user_id = int(line[0])
    first_order_day = line[2]
    last_order_day = line[3]

    all.append(user_id)

    first_orderday_interval = get_days_interval(first_order_day)
    last_orderday_interval = get_days_interval(last_order_day)

    thirty_day_orders = int(line[4])
    seven_day_orders = int(line[5])

    if first_orderday_interval <= 30:
        new.append(user_id)
    else:
        if thirty_day_orders == 0:
            lost.append(user_id)
            # print user_id, ',', last_orderday_interval
        else:
            if seven_day_orders == 0:
                now_not_active[user_id] = int(thirty_day_orders)
            else:
                now_active[user_id] = int(thirty_day_orders)

now = dict(now_active.items() + now_not_active.items())

median_order_num = median(now.values())

for item in now_active.keys():
    if now_active[item] > median_order_num:
        now_good_active.append(item)
    else:
        now_bad_active.append(item)

for item in now_not_active.keys():
    if now_not_active[item] > median_order_num:
        now_good_not_active.append(item)
    else:
        now_bad_not_active.append(item)


print len(all)
print len(new)
print len(now), round(len(now) * 100 / len(all), 2), '%'
print len(now_good_active)
print len(now_bad_active)
print len(now_good_not_active)
print len(now_bad_not_active)
print len(lost), round(len(lost) * 100 / len(all), 2), '%'
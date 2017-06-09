import os
import csv
import time, datetime


def day_str_to_datetime(day_str):
    t = time.strptime(day_str, "%Y-%m-%d")
    return datetime.datetime(*t[:3])


all_data = []

salers = {}

csv_file = csv.reader(file('orders.csv', 'rb'))

for data in csv_file:
    userid = int(data[0])

    if salers.has_key(userid) is False:
        salers[userid] = []

    order_day = data[1]
    order_num = int(data[2])

    order_info = {}
    order_info[order_day] = order_num

    salers[userid].append(order_info)

# print salers

csv_file = csv.reader(file('saler.csv', 'rb'))

# '"userid","nickname","status","kaitong","guwen","first_order_time","last_order_time","all_orders","datas"'

intervals = [1, 3, 7, 15, 30]

user_order_counts = {}

for data in csv_file:
    if data[0] == 'userid':
        continue

    userid = int(data[0])
    status = data[2]
    shoudan = data[6]
    kaitong = data[3]

    final_count = []

    if user_order_counts.has_key(userid) is False:
        user_order_counts[userid] = [0, 0, 0, 0, 0]

    if status == '1' and shoudan is not '' and salers.has_key(userid):
        for day_interval in intervals:

            order_counts = 0

            for order_info in salers[userid]:
                for order_day in order_info:

                    if ((day_str_to_datetime(order_day) - day_str_to_datetime(kaitong)).days <= day_interval -1):
                        order_counts += order_info[order_day]

            final_count.append(order_counts)

        user_order_counts[userid] = final_count


items = user_order_counts.items()
items.sort()

f = file('output.csv', "w+")

for k, v in items:
    line = str(k) + ','
    for num in v:
        line += str(num) + ','
    f.writelines(line + '\n')

f.close()

print 'done'






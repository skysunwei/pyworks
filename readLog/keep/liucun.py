# coding: utf-8

import csv

# source_files = ['buyer',
#                 'buyer_tel',
#                 'buyer_saler_841',
#                 'buyer_saler_237',
#                 'buyer_saler_typical',
#                 'buyer_tel_saler_typical']


def month_to_year_str_format(i):
    start_year_num = 2016
    month_of_year = 12

    month_str = '12月'
    year_str = str(start_year_num + (i - 1) / month_of_year) + '年'

    if i % month_of_year is not 0:
        month_str = str(i % month_of_year) + '月'

    return year_str + month_str


source_files = ['saler_17_10.csv']

output_file_names = []

current_month = 22
next_month = current_month + 1

for source_file in source_files:
    output_file_name = source_file + '_' + str(current_month) + '_liucun.csv'

    new_users = {}
    for i in range(1, next_month):
        new_users[i] = []

    users = {}
    for i in range(1, next_month):
        users[i] = []

    user_orders = {}

    stay_users = {}
    for i in range(1, next_month):
        stay_users[i] = []

    stay_users_orders = {}
    for i in range(1, next_month):
        stay_users_orders[i] = []

    stay_users_with_percent = {}
    for i in range(1, next_month):
        stay_users_with_percent[i] = []

    csv_file = csv.reader(file(source_file, 'rb'))

    lines = []
    for data in csv_file:
        lines.append(data)

    for line in lines:
        try:
            for i in range(1, len(line)):
                if int(line[i]) >0:
                    new_users[i].append(line[0])
                    break
        except:
            print source_file
            print line

    for line in lines:
        for i in range(1, len(line)):
            user_id = line[0]
            if user_orders.has_key(user_id) is False:
                user_orders[user_id] = []
            user_orders[user_id].append(int(line[i]))

    for line in lines:
        for i in range(1, len(line)):
            if int(line[i]) > 0:
                users[i].append(line[0])
                continue

    for i in new_users.keys():
        for j in users.keys():
            if j >= i:
                stay = len(set(new_users[i]).intersection(set(users[j])))
                # print stay
                stay_users[i].append(stay)

    for i in new_users.keys():
        for j in users.keys():
            if j >= i:
                order_num = 0
                stay_user_ids = list(set(new_users[i]).intersection(set(users[j])))
                for stay_user_id in stay_user_ids:
                    # print stay_user_id, i
                    # print user_orders[stay_user_id]
                    order_num += user_orders[stay_user_id][j - 1]
                # print i, j
                stay_users_orders[i].append(order_num)

    for stay_user in stay_users.keys():
        # print stay_users[stay_user]
        for i in range(0, len(stay_users[stay_user])):
            if stay_users[stay_user][i] is not 0:
                ava_order_str = str(round(float(stay_users_orders[stay_user][i]) / float(stay_users[stay_user][i]), 2))
            else:
                ava_order_str = ''

            if stay_users[stay_user][0] is not 0:
                percent_str = '(%.2f' % (stay_users[stay_user][i] * 100 / stay_users[stay_user][0]) + '%)'
            else:
                percent_str = '(0%)'

            if i is not 0:
                with_percent = str(stay_users[stay_user][i]) + '\n' + ava_order_str + '\n' + percent_str
                stay_users_with_percent[stay_user].append(with_percent)
            else:
                stay_users_with_percent[stay_user].append(str(stay_users[stay_user][i]) + '\n' + ava_order_str)

    # print stay_users_with_percent

    headline = ['月份']
    for i in range(1, next_month):
        headline.append(month_to_year_str_format(i))

    # print headline

    output_file = file(output_file_name, 'wb')
    writer = csv.writer(output_file)
    writer.writerow(headline)

    data = []

    for i in stay_users_with_percent.keys():
        data.append([month_to_year_str_format(i)] +
                    ['']*(current_month - len(stay_users_with_percent[i])) + stay_users_with_percent[i])

    # print data

    writer.writerows(data)

    output_file.close()

print 'done'

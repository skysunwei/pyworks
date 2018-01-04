# coding: utf-8

import csv

START_YEAR = 2016
MONTHS_OF_YEAR = 12

current_month = 25
source_files = {'buyer_17_11_all.csv': ['buyer_17_12.csv', 'buyer_18_1.csv']}
next_month = current_month + 1

KONG_MONTH = ['' for x in range(23)]


def month_to_year_str_format(i):
    month_str = '12月'
    year_str = str(START_YEAR + (i - 1) / MONTHS_OF_YEAR) + '年'

    if i % MONTHS_OF_YEAR is not 0:
        month_str = str(i % MONTHS_OF_YEAR) + '月'

    return year_str + month_str


def write_keep_file(stay_users, file_attach, stay_users_moneys):

    # generate file name
    output_file_name = source_file + '_' + str(current_month) + '_' + file_attach + '.csv'

    stay_users_with_percent = {}
    for i in range(1, next_month):
        stay_users_with_percent[i] = []

    for stay_user in stay_users.keys():
        # print stay_users[stay_user]
        for i in range(0, len(stay_users[stay_user])):
            stay_users_with_percent[stay_user].append(str(stay_users_moneys[stay_user][i]))

    # print stay_users_with_percent

    headline = ['月份']
    for i in range(1, next_month):
        headline.append(month_to_year_str_format(i))

    output_file = file(output_file_name, 'wb')
    writer = csv.writer(output_file)
    writer.writerow(headline)

    data = []

    for i in stay_users_with_percent.keys():
        data.append([month_to_year_str_format(i)] +
                    ['']*(current_month - len(stay_users_with_percent[i])) + stay_users_with_percent[i])

    writer.writerows(data)
    output_file.close()


def read_source_file():
    user_datas = {}

    for data in csv.reader(file(source_file, 'rb')):
        temp_data = data[0]
        data.remove(temp_data)
        user_datas[temp_data] = data

    for i in range(len(source_files[source_file])):
        addition_user_datas = {}

        for data in csv.reader(file(source_files[source_file][i], 'rb')):
            addition_user_datas[data[0]] = str(data[1])

        for key in user_datas.keys():
            if addition_user_datas.has_key(key):
                user_datas[key] += [addition_user_datas[key]]

        for key in addition_user_datas.keys():
            if user_datas.has_key(key) is False:
                user_datas[key] = []
                user_datas[key] += KONG_MONTH + ['' for x in range(i)] + [addition_user_datas[key]]

    return user_datas

for source_file in source_files.keys():

    new_users = {}
    for i in range(1, next_month):
        new_users[i] = []

    users = {}
    for i in range(1, next_month):
        users[i] = []

    user_orders = {}
    user_moneys = {}

    stay_users = {}
    for i in range(1, next_month):
        stay_users[i] = []

    stay_users_orders = {}
    for i in range(1, next_month):
        stay_users_orders[i] = []

    stay_users_moneys = {}
    for i in range(1, next_month):
        stay_users_moneys[i] = []

    user_datas = read_source_file()

    lines = []
    for key in user_datas.keys():
        lines.append([key] + user_datas[key])

    for line in lines:
        try:
            for i in range(1, len(line)):
                if '&' in line[i]:
                    new_users[i].append(line[0])
                    break
        except Exception, e:
            print line
            exit()

    for line in lines:
        for i in range(1, len(line)):
            user_id = line[0]

            the_order = 0
            the_money = 0.0

            if '&' in line[i]:
                order_and_money = line[i].split('&')
                the_order = int(order_and_money[0])
                the_money = float(order_and_money[1])

            if user_orders.has_key(user_id) is False:
                user_orders[user_id] = []
            user_orders[user_id].append(the_order)

            if user_moneys.has_key(user_id) is False:
                user_moneys[user_id] = []
            user_moneys[user_id].append(the_money)

    for line in lines:
        for i in range(1, len(line)):
            if '&' in line[i]:
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
                money_spend = 0.0
                stay_user_ids = list(set(new_users[i]).intersection(set(users[j])))
                for stay_user_id in stay_user_ids:
                    # print stay_user_id, i
                    # print user_orders[stay_user_id]
                    order_num += user_orders[stay_user_id][j - 1]
                    money_spend += user_moneys[stay_user_id][j - 1]

                # print i, j
                stay_users_orders[i].append(order_num)
                stay_users_moneys[i].append(money_spend)

    write_keep_file(stay_users, 'users', stay_users)
    write_keep_file(stay_users, 'orders', stay_users_orders)
    write_keep_file(stay_users, 'moneys', stay_users_moneys)

print 'done'

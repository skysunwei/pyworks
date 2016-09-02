# coding: utf-8

import csv

file_source = 'buyer'
output_file_name = file_source + '_liucun.csv'

current_month = 8
next_month = current_month + 1

new_users = {}
for i in range(1, next_month):
    new_users[i] = []

users = {}
for i in range(1, next_month):
    users[i] = []

stay_users = {}
for i in range(1, next_month):
    stay_users[i] = []

stay_users_with_percent = {}
for i in range(1, next_month):
    stay_users_with_percent[i] = []


for line in open(file_source):
    line_data = line.strip('\n').split(',')

    for i in range(1, len(line_data)):
        if int(line_data[i]) > 0:
            new_users[i].append(line_data[0])
            break

for line in open(file_source):
    line_data = line.strip('\n').split(',')

    for i in range(1, len(line_data)):
        if int(line_data[i]) > 0:
            users[i].append(line_data[0])
            continue

for i in new_users.keys():
    for j in users.keys():
        if j >= i:
            stay = len(set(new_users[i]).intersection(set(users[j])))
            # print stay
            stay_users[i].append(stay)


# format with %

for stay_user in stay_users.keys():
    # print stay_users[stay_user]
    for i in range(0, len(stay_users[stay_user])):
        if i is not 0:
            with_percent = str(stay_users[stay_user][i]) + '\n(' + \
                  "%.2f" %(stay_users[stay_user][i] * 100 / stay_users[stay_user][0]) + '%)'
            stay_users_with_percent[stay_user].append(with_percent)
        else:
            stay_users_with_percent[stay_user].append(stay_users[stay_user][i])
        # stay_users_with_percent.append()

# print stay_users_with_percent

headline = ['月份']
for i in range(1, next_month):
    headline.append(str(i) + '月')

# print headline

output_file = file(output_file_name, 'wb')
writer = csv.writer(output_file)
writer.writerow(headline)

data = []

for i in stay_users_with_percent.keys():
    data.append([str(i) + '月'] +
                ['']*(current_month - len(stay_users_with_percent[i])) + stay_users_with_percent[i])

# print data

writer.writerows(data)

output_file.close()
